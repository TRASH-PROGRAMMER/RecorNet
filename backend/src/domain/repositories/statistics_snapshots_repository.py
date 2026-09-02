from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.statistics_snapshots import StatisticsSnapshot

class StatisticsSnapshotRepository(ABC):
    @abstractmethod
    def save(self, statistics_snapshot: StatisticsSnapshot) -> StatisticsSnapshot:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, statistics_snapshot_id: str) -> Optional[StatisticsSnapshot]:
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[StatisticsSnapshot]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, statistics_snapshot_id: str) -> bool:
        raise NotImplementedError