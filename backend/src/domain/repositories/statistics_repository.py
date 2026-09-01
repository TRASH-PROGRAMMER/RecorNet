from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from src.domain.entities.statistics_snapshots import StatisticsSnapshots


# pyre-ignore [13]
#Clase para representar el repositorio de estadisticas
class StatisticsRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para obtener estadisticas
    def get_by_patient(self, patient_id: str) -> Dict[str, float]:
        raise NotImplementedError
    # Metodos para guardar estadisticas
    @abstractmethod
    def get_by_id(self, snapshot_id: str) -> Optional[StatisticsSnapshots]:
        raise NotImplementedError
    # Metodos para obtener estadisticas
    @abstractmethod
    def get_for_patient(self, patient_id: str) -> List[StatisticsSnapshots]:
        raise NotImplementedError
    # Metodos para eliminar estadisticas
    @abstractmethod
    def delete(self, snapshot_id: str) -> bool:
        raise NotImplementedError
    # Metodos para guardar estadisticas
    @abstractmethod
    def save(self, snapshot: StatisticsSnapshots) -> StatisticsSnapshots:
        raise NotImplementedError    
