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
    recipient_user_id: str = "" # usuario destinatario de la notificación
    title: str = "" # titulo de la notificación
    type: NotificationType = NotificationType.REMINDER # tipo de notificación
    message: str = "" # mensaje de la notificación
    channel: NotificationChannel = NotificationChannel.PUSH # canal de notificación
    delivery_status:  NotificationStatus = NotificationStatus.PENDING # estado de la notificación
    sent_at: Optional[datetime] = None # fecha de envío de la notificación
    read_at: Optional[datetime] = None # fecha de lectura de la notificación
    delivery_at: Optional[datetime] = None # fecha de entrega de la notificación
    failure_reason: str = "" # razón de la falla de la notificación
    

    def mark_as_sent(self): # marca la notificación como enviada
        self.status = NotificationStatus.SENT
        self.sent_at = datetime.utcnow()
    def mark_as_read(self): # marca la notificación como leída
        self.status = NotificationStatus.READ
        self.read_at = datetime.utcnow()

    def mark_as_failed(self): # marca la notificación como fallida
        self.status = NotificationStatus.FAILED
        
    def mark_as_delivered(self): # marca la notificación como entregada
        self.status = NotificationStatus.DELIVERED
        
    def mark_as_opened(self):   # marca la notificación como abierta
        self.status = NotificationStatus.OPENED
        