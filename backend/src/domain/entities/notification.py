from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from src.domain.value_objects.idempotency_key import IdempotencyKey
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
    SMS = "sms"
    
  

# clase para representar una notificación

@dataclass
class Notification:
    id: Optional[str] = None
    user_id: str = "" 
    dose_event_id: IdempotencyKey = field(default_factory=lambda: IdempotencyKey(""))   
    title: str = ""
    type: NotificationType = NotificationType.REMINDER
    message: str = ""
    channel: NotificationChannel = NotificationChannel.PUSH
    status:  NotificationStatus = NotificationStatus.PENDING
    sent_at: Optional[datetime] = None
    read_at: Optional[datetime] = None