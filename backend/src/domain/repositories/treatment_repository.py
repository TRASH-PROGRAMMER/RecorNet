from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.treatment import Treatment

# clase abstracta para el repositorio de tratamientos
class TreatmentRepository(ABC):
    # metodo para guardar un tratamiento
    @abstractmethod
    def save(self, treatment: Treatment, actor_id: str) -> Treatment:
        raise NotImplementedError
# metodo para obtener un tratamiento por id
    @abstractmethod
    def get_by_id(
        self,
        treatment_id: str,
        *,
        actor_id: str,
        permission: str = "view_treatment",
    ) -> Optional[Treatment]:
        raise NotImplementedError
# metodo para obtener tratamientos por id de paciente
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
