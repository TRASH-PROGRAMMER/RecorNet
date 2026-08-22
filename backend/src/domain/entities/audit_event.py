from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional
from uuid import uuid4


class AuditAction(str, Enum):
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    STATUS_TRANSITION = "status_transition"
    ACCESS = "access"
    DELIVERY = "delivery"


@dataclass
class AuditEvent:
    """Registro inmutable de una acción relevante para seguridad y trazabilidad."""

    id: str = field(default_factory=lambda: str(uuid4()))
    actor_user_id: Optional[str] = None
    action: AuditAction = AuditAction.ACCESS
    aggregate_type: str = ""
    aggregate_id: str = ""
    correlation_id: Optional[str] = None
    metadata: dict[str, Any] = field(default_factory=dict)
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
