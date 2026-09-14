from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from src.domain.entities.sync_operation import SyncOperation

class SyncOperationRepository(ABC):
    @abstractmethod
    def save(self, sync_operation: SyncOperation) -> SyncOperation:
        """Guarda una operación de sincronización"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, sync_operation_id: str) -> Optional[SyncOperation]:
        """Obtiene una operación de sincronización por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_pending_for_user(self, user_id: str) -> List[SyncOperation]:
        """Obtiene las operaciones de sincronización pendientes para un usuario"""
        raise NotImplementedError
    @abstractmethod
    def get_unacknowledged_for_user(self, user_id: str) -> List[SyncOperation]:
        """Obtiene las operaciones de sincronización no confirmadas para un usuario"""
        raise NotImplementedError    
    @abstractmethod
    def mark_as_completed(self, sync_operation_id: str) -> bool:
        """Marca una operación de sincronización como completada"""
        raise NotImplementedError
    @abstractmethod
    def mark_as_failed(self, sync_operation_id: str) -> bool:
        """Marca una operación de sincronización como fallida"""
        raise NotImplementedError
    @abstractmethod
    def delete_old_completed(self, user_id: str, days: int) -> int:
        """Elimina operaciones de sincronización completadas y antiguas para un usuario"""
        raise NotImplementedError
    @abstractmethod
    def acknowledge_all(self, sync_operation_ids: List[str]) -> bool:
        """Confirma que un lote de operaciones de sincronización ha sido recibido y procesado"""
        raise NotImplementedError
        