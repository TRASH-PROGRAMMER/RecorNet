from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.statistics_snapshots import StatisticsSnapshots
from src.domain.repositories.statistics_repository import StatisticsRepository

# Alias de compatibilidad
Statistics = StatisticsSnapshots


# pyre-ignore [13]
# Clase para representar el servicio de estadísticas
class StatisticsService(ABC):
    # @abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para obtener estadísticas
    def get_by_id(self, statistics_id: str) -> Optional[StatisticsSnapshots]:
        """Obtiene estadísticas por su ID"""
        raise NotImplementedError

    # Metodos para actualizar estadísticas
    @abstractmethod
    def update(self, statistics_id: str, statistics: StatisticsSnapshots) -> Optional[StatisticsSnapshots]:
        """Actualiza estadísticas"""
        raise NotImplementedError

    # Metodos para eliminar estadísticas
    @abstractmethod
    def delete(self, statistics_id: str) -> bool:
        """Elimina estadísticas"""
        raise NotImplementedError

    # Metodos para obtener estadísticas pendientes
    @abstractmethod
    def get_pending(self) -> List[StatisticsSnapshots]:
        """Obtiene las estadísticas pendientes"""
        raise NotImplementedError
