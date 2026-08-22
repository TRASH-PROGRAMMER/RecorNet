from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional
from uuid import uuid4


class SyncOperationStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"


@dataclass
class SyncOperation:
    """Operación persistida de la cola offline para procesarla con idempotencia."""

    user_id: str
    aggregate_type: str
    aggregate_id: str
    operation_type: str
    idempotency_key: str
    payload: dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(uuid4()))
    status: SyncOperationStatus = SyncOperationStatus.PENDING
    attempt_count: int = 0
    last_error: Optional[str] = None
    next_attempt_at: Optional[datetime] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def register_failure(self, error: str, next_attempt_at: Optional[datetime] = None) -> None:
        self.status = SyncOperationStatus.FAILED
        self.attempt_count += 1
        self.last_error = error
        self.next_attempt_at = next_attempt_at
