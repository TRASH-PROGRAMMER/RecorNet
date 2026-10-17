from __future__ import annotations  #  anotaciones para que el código sea más legible y se pueda hacer un chequeo de tipos

from datetime import datetime, timezone

from sqlalchemy import and_, or_, select
from sqlalchemy.orm import Session

from src.domain.entities.medication import Medication
from src.domain.exceptions.domain_exceptions import UnauthorizedAccess
from src.domain.repositories.medication_repository import MedicationRepository
from src.infrastructure.persistence.models.recornet import (
    CarePermissionModel,
    CareRelationshipModel,
    MedicationModel,
    TreatmentModel,
)
from src.infrastructure.persistence.repositories._authorized import (
    authorization_clause,
    int_id,
    map_medication,
    require_authorized,
)

# clase para la persistencia de medicamentos
class SqlAlchemyMedicationRepository(MedicationRepository):
    """Persistencia de medicamentos; el alcance por paciente pasa por treatments."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, medication: Medication, actor_id: str) -> Medication:
        actor = int_id(actor_id)
        model = (
            self._session.get(MedicationModel, int(medication.id))
            if medication.id is not None
            else None
        )
        if model is None:
            model = MedicationModel(
                name=medication.name,
                description=medication.description,
                photo_url=medication.photo_url,
                form=medication.form,
                manufacturer=medication.manufacturer,
                created_by_user_id=actor,
                created_at=medication.created_at or datetime.now(timezone.utc),
                status=medication.status.value,
            )
            self._session.add(model)
        else:
            if model.created_by_user_id != actor:
                # Un medicamento es un registro de catálogo; las actualizaciones están restringidas a su creador
                # hasta que un caso de uso de nivel superior proporcione un contexto de paciente.
                raise UnauthorizedAccess(
                    f"actor {actor_id} cannot update medication {medication.id}"
                )
            model.name = medication.name
            model.description = medication.description
            model.photo_url = medication.photo_url
            model.form = medication.form
            model.manufacturer = medication.manufacturer
            model.status = medication.status.value
        self._session.flush()
        return map_medication(model)


    
    # statement para obtener medicamentos autorizados
    def _authorized_medication_statement(self, patient_id: str, actor_id: str, permission: str):
        return (
            select(MedicationModel)
            .join(TreatmentModel, TreatmentModel.medication_id == MedicationModel.id)
            .outerjoin(
                CareRelationshipModel,
                CareRelationshipModel.elderly_id == TreatmentModel.patient_user_id,
            )
            .outerjoin(
                CarePermissionModel,
                CarePermissionModel.care_relationship_id == CareRelationshipModel.id,
            )
            .where(
                TreatmentModel.patient_user_id == int_id(patient_id),
                authorization_clause(patient_id, actor_id, permission),
            )
            .distinct()
        )

    def get_by_id(
        self,
        medication_id: str,
        *,
        actor_id: str,
        patient_id: str | None = None,
        permission: str = "view_medication",
    ) -> Medication | None:
        if patient_id is None:
            model = self._session.scalar(
                select(MedicationModel).where(
                    MedicationModel.id == int_id(medication_id),
                    MedicationModel.created_by_user_id == int_id(actor_id),
                )
            )
        else:
            model = self._session.scalar(
                self._authorized_medication_statement(patient_id, actor_id, permission).where(
                    MedicationModel.id == int_id(medication_id)
                )
            )
        return map_medication(model) if model else None

    # obtiene los medicamentos autorizados para un paciente
    def get_for_patient(self, patient_id: str, *, actor_id: str, permission: str = "view_medication") -> list[Medication]:
        return [
            map_medication(model)
            for model in self._session.scalars(
                self._authorized_medication_statement(patient_id, actor_id, permission)
            ).all()
        ]
    
    # elimina un medicamento
    def delete(self, medication_id: str, *, actor_id: str, patient_id: str) -> bool:
        require_authorized(self._session, patient_id, actor_id, "manage_treatments")
        model = self._session.scalar(
            select(MedicationModel)
            .join(TreatmentModel, TreatmentModel.medication_id == MedicationModel.id)
            .where(
                MedicationModel.id == int_id(medication_id),
                TreatmentModel.patient_user_id == int_id(patient_id),
            )
        )
        if model is None:
            return False
        self._session.delete(model)
        self._session.flush()
        return True
