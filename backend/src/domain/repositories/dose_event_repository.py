from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from src.domain.entities.dose_events import DoseEvent
# clase para representar el repositorio de eventos de dosis
# @abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
class DoseEventRepository(ABC):
    """Clase abstracta para representar el repositorio de eventos de dosis"""
    #Metodos abstractos para manejar los eventos de dosis
    @abstractmethod
    def save(self, dose_event: DoseEvent) -> DoseEvent:
        """Guarda un evento de dosis en la base de datos"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, dose_event_id: str) -> Optional[DoseEvent]:
        """Obtiene un evento de dosis por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_by_idempotency_key(self, idempotency_key: str) -> Optional[DoseEvent]:
        """Obtiene un evento de dosis por su clave de idempotencia"""
        raise NotImplementedError
    @abstractmethod
    def get_history_for_patient(self, patient_id: str,*,from_date: datetime,to_date:datetime,actor_id: str, permission:str = "view_dose_events") -> List[DoseEvent]:
        """Obtiene todos los eventos de dosis de un paciente"""
        raise NotImplementedError
    @abstractmethod
    def get_pending_for_patient(self, caregiver_id: str) -> List[DoseEvent]:
        """Obtiene todos los eventos de dosis pendientes para un paciente"""
        raise NotImplementedError
    @abstractmethod
    def get_for_patient(self, patient_id: str) -> List[DoseEvent]:
        """Obtiene todos los historiales de un paciente"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, history_id: str) -> bool:
        """Elimina un historial"""
        raise NotImplementedError
