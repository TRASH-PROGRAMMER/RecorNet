# pyrefly: ignore [missing-import]
from src.domain.repositories.notification_delivery_repository import NotificationDeliveryRepository
from src.domain.repositories.notification_policy_repository import NotificationPolicyRepository
from src.domain.repositories.reminder_times_repository import ReminderTimesRepository

# pyre-ignore [13]
# Clase para representar el servicio de notificación
class NotificationService:
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar notificaciones
    def save(self, notification: Notification) -> Notification:
        """Guarda una notificación"""
        raise NotImplementedError
    # Metodos para obtener notificaciones
    @abstractmethod
    def get_by_id(self, notification_id: str) -> Optional[Notification]:
        """Obtiene una notificación por su ID"""
        raise NotImplementedError
    # Metodos para actualizar notificaciones
    @abstractmethod
    def update(self, notification_id: str, notification: Notification) -> Optional[Notification]:
        """Actualiza una notificación"""
        raise NotImplementedError
    # Metodos para eliminar notificaciones
    @abstractmethod
    def delete(self, notification_id: str) -> bool:
        """Elimina una notificación"""
        raise NotImplementedError
    # Metodos para enviar notificaciones
    @abstractmethod
    def send(self, notification: Notification) -> bool:
        """Envía una notificación"""
        raise NotImplementedError
    # Metodos para obtener notificaciones pendientes
    @abstractmethod
    def get_pending(self) -> List[Notification]:
        """Obtiene las notificaciones pendientes"""
        raise NotImplementedError