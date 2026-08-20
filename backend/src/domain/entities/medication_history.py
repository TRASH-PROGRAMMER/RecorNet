from dataclasses import field
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.domain.value_objects.idempotency_key import IdempotencyKey
from enum import Enum

# clase para representar el estado del evento de dosis
class DoseEventStatus(str, Enum):
    SCHEDULED = "scheduled"
    ALERTED = "alerted"
    TAKEN = "taken"
    PENDING = "pending"
    SKIPPED = "skipped"
    FAILED = "failed"
    SYNCED = "synced"

# clase para registrar los eventos de dosis
@dataclass
class DoseEvent: 
    id: Optional[str] = None
    idempotency_key: IdempotencyKey = field(default_factory=lambda: IdempotencyKey("")) 
    reminder_schedule_id: str = ""
    treatment_id: str = ""
    user_id: str = ""
    scheduled_at: datetime = None
    taken_at: Optional[datetime] = None
    status: DoseEventStatus = DoseEventStatus.SCHEDULED 
    def change_status(self, status: DoseEventStatus):
        self.status = status
        if status == DoseEventStatus.TAKEN:
            self.taken_at = datetime.now()
        
