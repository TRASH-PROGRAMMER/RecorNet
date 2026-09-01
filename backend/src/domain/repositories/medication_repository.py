from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.medication import Medication


class MedicationRepository(ABC):
    @abstractmethod
    def save(self, medication: Medication, actor_id: str) -> Medication:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        medication_id: str,
        *,
        actor_id: str,
        patient_id: Optional[str] = None,
        permission: str = "view_medication",
    ) -> Optional[Medication]:
        """La consulta debe validar la relación si patient_id pertenece a un adulto mayor."""
        raise NotImplementedError

    @abstractmethod
    def get_for_patient(
        self,
        patient_id: str,
        *,
        actor_id: str,
        permission: str = "view_medication",
    ) -> List[Medication]:
        """Devuelve medicamentos solo dentro del contexto autorizado del paciente."""
        raise NotImplementedError

    @abstractmethod
    def delete(self, medication_id: str, *, actor_id: str, patient_id: str) -> bool:
        raise NotImplementedError
