from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import uuid4


class NotificationDeliveryStatus(str, Enum):
    QUEUED = "queued"
    SENT = "sent"
    DELIVERED = "delivered"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class NotificationDelivery:
    """Intento individual de entregar una notificación a un dispositivo o canal."""

    notification_id: str
    id: str = field(default_factory=lambda: str(uuid4()))
    device_id: Optional[str] = None
    attempt_number: int = 1
    status: NotificationDeliveryStatus = NotificationDeliveryStatus.QUEUED
    provider_message_id: Optional[str] = None
    attempted_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    failure_reason: Optional[str] = None

    def mark_sent(self, at: Optional[datetime] = None) -> None:
        self.status = NotificationDeliveryStatus.SENT
        self.attempted_at = at or datetime.now(timezone.utc)

    def mark_delivered(self, at: Optional[datetime] = None) -> None:
        self.status = NotificationDeliveryStatus.DELIVERED
        self.delivered_at = at or datetime.now(timezone.utc)

    def mark_failed(self, reason: str) -> None:
        self.status = NotificationDeliveryStatus.FAILED
        self.failure_reason = reason
