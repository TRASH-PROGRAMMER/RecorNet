from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4


@dataclass
class DoseStatusTransition:
    """Transición inmutable de una dosis que conserva el historial de su ciclo de vida."""

    dose_event_id: str
    from_status: Optional[str]
    to_status: str
    id: str = field(default_factory=lambda: str(uuid4()))
    changed_by_user_id: Optional[str] = None
    reason: Optional[str] = None
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
