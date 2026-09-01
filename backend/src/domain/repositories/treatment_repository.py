from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.treatment import Treatment


class TreatmentRepository(ABC):
    @abstractmethod
    def save(self, treatment: Treatment, actor_id: str) -> Treatment:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        treatment_id: str,
        *,
        actor_id: str,
        permission: str = "view_treatment",
    ) -> Optional[Treatment]:
        raise NotImplementedError

    @abstractmethod
    def get_by_patient_id(
        self,
        patient_id: str,
        *,
        actor_id: str,
        permission: str = "view_treatment",
    ) -> List[Treatment]:
        """Solo devuelve tratamientos si actor_id está autorizado sobre patient_id."""
        raise NotImplementedError
