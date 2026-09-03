from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.medication import Medication


class MedicationRepository(ABC):
    """Clase abstracta para representar el repositorio de medicamentos"""
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar, obtener, actualizar y eliminar medicamentos
    def save(self, medication: Medication, actor_id: str) -> Medication:
        """Guarda un medicamento en la base de datos"""
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
        """Obtiene un medicamento por su ID"""
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
