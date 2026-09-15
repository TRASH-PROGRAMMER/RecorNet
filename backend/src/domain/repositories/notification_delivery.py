from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.notification_delivery import NotificationDelivery

# pyre-ignore [13]
# Clase para representar el repositorio de entregas de notificación
class NotificationDeliveryRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar entregas de notificación
    def save(self, notification_delivery: NotificationDelivery) -> NotificationDelivery:
        """Guarda una entrega de notificación"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, notification_delivery_id: str) -> Optional[NotificationDelivery]:
        """Obtiene una entrega de notificación por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_notification(self, notification_id: str) -> List[NotificationDelivery]:
        """Obtiene las entregas de notificación de una notificación"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[NotificationDelivery]:
        """Obtiene las entregas de notificación de un usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, notification_delivery_id: str) -> bool:
        """Elimina una entrega de notificación"""
        raise NotImplementedError    