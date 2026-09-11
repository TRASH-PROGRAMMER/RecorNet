from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.statistics_snapshots import StatisticsSnapshots

class StatisticsSnapshotRepository(ABC):
    """
    Puerto de persistencia para instantáneas de estadísticas.
    """
    @abstractmethod
    def save(self, statistics_snapshot: StatisticsSnapshots) -> StatisticsSnapshots:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, statistics_snapshot_id: str) -> Optional[StatisticsSnapshots]:
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[StatisticsSnapshots]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, statistics_snapshot_id: str) -> bool:
        raise NotImplementedError