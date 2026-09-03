from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.dose_events import DoseEvent
#Clase para representar el repositorio de historiales
class HistoryRepository(ABC):
    """Clase abstracta para representar el repositorio de historiales"""
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar, obtener, actualizar y eliminar historiales
    def save(self, history: DoseEvent) -> DoseEvent:
        """Guarda un historial en la base de datos"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, history_id: str) -> Optional[DoseEvent]:
        """Obtiene un historial por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_patient(self, patient_id: str) -> List[DoseEvent]:
        """Obtiene todos los historiales de un paciente"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, history_id: str) -> bool:
        """Elimina un historial"""
        raise NotImplementedError
        