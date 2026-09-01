from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.dose_events import DoseEvent
#Clase para representar el repositorio de historiales
class HistoryRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar, obtener, actualizar y eliminar historiales
    def save(self, history: DoseEvent) -> DoseEvent:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, history_id: str) -> Optional[DoseEvent]:
        raise NotImplementedError
    @abstractmethod
    def get_for_patient(self, patient_id: str) -> List[DoseEvent]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, history_id: str) -> bool:
        raise NotImplementedError
        