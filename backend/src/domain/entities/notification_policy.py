from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from uuid import uuid4


class EscalationTarget(str, Enum):
    PATIENT = "patient"
    CAREGIVER = "caregiver"


@dataclass
class NotificationPolicy:
    """Reglas de repetición y escalamiento aplicables a un tratamiento o usuario."""

    owner_user_id: str
    id: str = field(default_factory=lambda: str(uuid4()))
    treatment_id: Optional[str] = None
    repeat_interval_minutes: int = 10
    max_retries: int = 3
    pending_after_minutes: int = 30
    escalation_target: EscalationTarget = EscalationTarget.CAREGIVER
    enabled: bool = True

    def validate(self) -> None:
        if self.repeat_interval_minutes <= 0:
            raise ValueError("repeat_interval_minutes must be positive")
        if self.max_retries < 0:
            raise ValueError("max_retries cannot be negative")
        if self.pending_after_minutes < self.repeat_interval_minutes:
            raise ValueError("pending_after_minutes must allow at least one reminder")
