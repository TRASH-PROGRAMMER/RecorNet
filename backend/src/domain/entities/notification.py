from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# clase para representar una notificación
@dataclass
class Notification:
    id: Optional[str] = None
    user_id: str = ""
    dose_event_id: Optional[str] = None
    type: str = ""
    message: str = ""
    sent_at: datetime = field(default_factory=datetime.utcnow)
    read_at: Optional[datetime] = None
