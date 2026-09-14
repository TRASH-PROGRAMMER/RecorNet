from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.notification import Notification

class NotificationRepository(ABC):
    """Repositorio de notificaciones"""
    @abstractmethod
    def save(self, notification: Notification) -> Notification:
        """Guarda una notificación"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, notification_id: str) -> Optional[Notification]:
        """Obtiene una notificación por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[Notification]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, notification_id: str) -> bool:
        raise NotImplementedError