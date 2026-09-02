from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.dose_events import DoseEvent
# clase para re
class DoseEventRepository(ABC):
    @abstractmethod
    def save(self, dose_event: DoseEvent) -> DoseEvent:
        """Guarda un evento de dosis en la base de datos"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, dose_event_id: str) -> Optional[DoseEvent]:
        """Obtiene un evento de dosis por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[DoseEvent]:
        """Obtiene todos los eventos de dosis de un usuario"""
        
        raise NotImplementedError
    @abstractmethod
    def delete(self, dose_event_id: str) -> bool:
        """Elimina un evento de dosis"""
        raise NotImplementedError
