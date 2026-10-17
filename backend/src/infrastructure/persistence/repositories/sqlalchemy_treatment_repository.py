from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.domain.entities.treatment import Treatment
from src.domain.repositories.treatment_repository import TreatmentRepository
from src.domain.exceptions.domain_exceptions import UnauthorizedAccess
from src.infrastructure.persistence.models.recornet import (
    CarePermissionModel,
    CareRelationshipModel,
    TreatmentModel,
)
from src.infrastructure.persistence.repositories._authorized import (
    authorization_clause,
    int_id,
    map_treatment,
    normalize_permission,
    require_authorized,
)


class SqlAlchemyTreatmentRepository(TreatmentRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def _authorized_statement(self, patient_id: str | int, actor_id: str | int, permission: str):
        return (
            select(TreatmentModel)
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
        )

    def save(self, treatment: Treatment, actor_id: str) -> Treatment:
        patient_id = treatment.patient_user_id
        require_authorized(self._session, patient_id, actor_id, "manage_treatments")
        model = (
            self._session.get(TreatmentModel, int(treatment.id))
            if treatment.id is not None
            else None
        )
        dose = f"{treatment.dosage.amount:g} {treatment.dosage.unit}".strip()
        if model is None:
            model = TreatmentModel(
                medication_id=int(treatment.medication_id),
                patient_user_id=int(treatment.patient_user_id),
                creator_user_id=int(treatment.created_by_user_id or actor_id),
                dose=dose,
                instructions=treatment.instructions,
                frequency_value=treatment.frequency.interval.value,
                frequency_unit=treatment.frequency.interval.unit.value,
                start_date=treatment.start_date,
                end_date=treatment.end_date,
                version=max(1, treatment.version),
                status=treatment.status.value,
            )
            self._session.add(model)
        else:
            model.dose = dose
            model.instructions = treatment.instructions
            model.frequency_value = treatment.frequency.interval.value
            model.frequency_unit = treatment.frequency.interval.unit.value
            model.start_date = treatment.start_date
            model.end_date = treatment.end_date
            model.version = treatment.version
            model.status = treatment.status.value
        self._session.flush()
        return map_treatment(model)

    def get_by_id(
        self,
        treatment_id: str,
        *,
        actor_id: str,
        permission: str = "view_treatment",
    ) -> Treatment | None:
        # The patient id is intentionally obtained only after the authorized query: callers
        # cannot use an arbitrary treatment id to discover a non-linked patient's record.
        model = self._session.scalar(
            select(TreatmentModel)
            .outerjoin(
                CareRelationshipModel,
                CareRelationshipModel.elderly_id == TreatmentModel.patient_user_id,
            )
            .outerjoin(
                CarePermissionModel,
                CarePermissionModel.care_relationship_id == CareRelationshipModel.id,
            )
            .where(
                TreatmentModel.id == int_id(treatment_id),
                (
                    TreatmentModel.patient_user_id == int_id(actor_id)
                )
                | (
                    (CareRelationshipModel.caregiver_id == int_id(actor_id))
                    & (CareRelationshipModel.status == "active")
                    & (CarePermissionModel.code == normalize_permission(permission))
                    & CarePermissionModel.revoked_at.is_(None)
                ),
            )
        )
        return map_treatment(model) if model else None

    def get_by_patient_id(
        self,
        patient_id: str,
        *,
        actor_id: str,
        permission: str = "view_treatment",
    ) -> list[Treatment]:
        return [
            map_treatment(model)
            for model in self._session.scalars(
                self._authorized_statement(patient_id, actor_id, permission)
            ).all()
        ]
