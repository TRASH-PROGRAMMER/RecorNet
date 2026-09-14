from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.statistics_snapshots import StatisticsSnapshots

class StatisticsSnapshotRepository(ABC):
    """
    Puerto de persistencia para instantáneas de estadísticas.
    """
    @abstractmethod
    def save(self, statistics_snapshot: StatisticsSnapshots) -> StatisticsSnapshots:
        """Guarda una instantánea de estadísticas"""
        raise NotImplementedError
    @abstractmethod
    def get_latest_for_patient(self, patient_id: str, *, actor_id: str, permission: str = "view_statistics") -> Optional[StatisticsSnapshots]:
        """Obtiene la última instantánea de estadísticas para un paciente"""
        raise NotImplementedError
    @abstractmethod
    def get_history_for_patient(self, patient_id: str, *, actor_id: str, permission: str = "view_statistics") -> List[StatisticsSnapshots]:
        """Obtiene el historial de instantáneas de estadísticas para un paciente"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, statistics_snapshot_id: str) -> bool:
        """Elimina una instantánea de estadísticas"""
        raise NotImplementedError