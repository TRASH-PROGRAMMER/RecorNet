from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
from enum import Enum

# clase para representar el tipo de notificación
class NotificationType(str, Enum):
    REMINDER = "reminder"
    CONFIRMATION = "confirmation"
    MISSED = "missed"
    INFO = "info"

# clase para representar el estado de la notificación
class NotificationStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    READ = "read"
    FAILED = "failed"
    DELIVERED = "delivered"
    OPENED = "opened"

# clase para representar el canal de notificación
class NotificationChannel(str, Enum):
    PUSH = "push"
    LOCAL = "local"
    
  

# clase para representar una notificación

@dataclass
class Notification:
    id: Optional[str] = None
    dose_event_id: Optional[str] = None
    recipient_user_id: str = "" # usuario destinatario de la notificación
    title: str = "" # titulo de la notificación
    type: NotificationType = NotificationType.REMINDER # tipo de notificación
    message: str = "" # mensaje de la notificación
    channel: NotificationChannel = NotificationChannel.PUSH # canal de notificación
    status: NotificationStatus = NotificationStatus.PENDING
    sent_at: Optional[datetime] = None # fecha de envío de la notificación
    read_at: Optional[datetime] = None # fecha de lectura de la notificación
    delivered_at: Optional[datetime] = None # fecha de entrega de la notificación
    failure_reason: Optional[str] = None # razón de la falla de la notificación

    @property
    def delivery_status(self) -> NotificationStatus:
        """Alias de lectura mientras la entrega detallada vive en NotificationDelivery."""
        return self.status

    def mark_as_sent(self) -> None:
        self.status = NotificationStatus.SENT
        self.sent_at = datetime.now(timezone.utc)

    def mark_as_read(self) -> None:
        self.status = NotificationStatus.READ
        self.read_at = datetime.now(timezone.utc)

    def mark_as_failed(self, reason: str) -> None:
        self.status = NotificationStatus.FAILED
        self.failure_reason = reason

    def mark_as_delivered(self) -> None:
        self.status = NotificationStatus.DELIVERED
        self.delivered_at = datetime.now(timezone.utc)

    def mark_as_opened(self) -> None:
        self.status = NotificationStatus.OPENED
