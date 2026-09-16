from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.dose_status_transition import DoseStatusTransition

# pyre-ignore [13]
# Clase para representar el repositorio de transiciones de estado de dosis
class DoseStatusTransitionRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar transiciones de estado de dosis
    def save(self, dose_status_transition: DoseStatusTransition) -> DoseStatusTransition:
        """Guarda una transición de estado de dosis"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, dose_status_transition_id: str) -> Optional[DoseStatusTransition]:
        """Obtiene una transición de estado de dosis por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_dose(self, dose_id: str) -> List[DoseStatusTransition]:
        """Obtiene las transiciones de estado de dosis de una dosis"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[DoseStatusTransition]:
        """Obtiene las transiciones de estado de dosis de un usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, dose_status_transition_id: str) -> bool:
        """Elimina una transición de estado de dosis"""
        raise NotImplementedError