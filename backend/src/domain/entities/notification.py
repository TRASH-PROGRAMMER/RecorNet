from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from src.domain.value_objects.idempotency_key import IdempotencyKey

# clase para representar una notificación

@dataclass
class Notification:
    id: Optional[str] = None
    user_id: str = "" 
    dose_event_id: IdempotencyKey = field(default_factory=lambda: IdempotencyKey(""))   
    type: str = ""
    message: str = ""
    sent_at: datetime = field(default_factory=datetime.utcnow)
    read_at: Optional[datetime] = None