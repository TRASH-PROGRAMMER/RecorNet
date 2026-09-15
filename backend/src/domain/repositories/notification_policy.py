from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.notification_policy import NotificationPolicy

# pyre-ignore [13]
# Clase para representar el repositorio de políticas de notificación
class NotificationPolicyRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar políticas de notificación
    def save(self, notification_policy: NotificationPolicy) -> NotificationPolicy:
        """Guarda una política de notificación"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, notification_policy_id: str) -> Optional[NotificationPolicy]:
        """Obtiene una política de notificación por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[NotificationPolicy]:
        """Obtiene las políticas de notificación de un usuario"""
        raise NotImplementedError
    @abstractmethod
    def get_for_elderly(self, elderly_id: str) -> List[NotificationPolicy]:
        """Obtiene las políticas de notificación de un adulto mayor"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, notification_policy_id: str) -> bool:
        """Elimina una política de notificación"""
        raise NotImplementedError    