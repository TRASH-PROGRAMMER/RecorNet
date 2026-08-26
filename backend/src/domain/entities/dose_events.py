from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import uuid4

from src.domain.value_objects.idempotency_key import IdempotencyKey


class DoseEventStatus(str, Enum):
    SCHEDULED = "scheduled"
    ALERTED = "alerted"
    TAKEN = "taken"
    PENDING = "pending"
    SKIPPED = "skipped"


class SyncStatus(str, Enum):
    PENDING = "pending"
    SYNCED = "synced"
    FAILED = "failed"


class Source(str, Enum):
    CLIENT = "client"
    BACKEND = "backend"
    MOBILE = "mobile"
    API = "api"


@dataclass
class DoseEvent:
    """Instancia de una dosis con ciclo clínico y sincronización separados."""

    id: Optional[str] = None
    treatment_id: str = ""
    schedule_id: str = ""
    idempotency_key: IdempotencyKey = field(default_factory=IdempotencyKey)
    scheduled_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    status: DoseEventStatus = DoseEventStatus.SCHEDULED
    sync_status: SyncStatus = SyncStatus.PENDING
    confirmed_at: Optional[datetime] = None
    source: Source = Source.CLIENT

    def __post_init__(self) -> None:
        if self.id is None:
            self.id = str(uuid4())

    def transition_to(self, next_status: DoseEventStatus) -> None:
        allowed_transitions = {
            DoseEventStatus.SCHEDULED: {DoseEventStatus.ALERTED},
            DoseEventStatus.ALERTED: {DoseEventStatus.TAKEN, DoseEventStatus.PENDING},
            DoseEventStatus.PENDING: {DoseEventStatus.ALERTED, DoseEventStatus.SKIPPED},
            DoseEventStatus.TAKEN: set(),
            DoseEventStatus.SKIPPED: set(),
        }
        if next_status not in allowed_transitions[self.status]:
            raise ValueError(f"invalid dose status transition: {self.status} -> {next_status}")
        self.status = next_status
        if next_status == DoseEventStatus.TAKEN:
            self.confirmed_at = datetime.now(timezone.utc)

    def mark_alerted(self) -> None:
        self.transition_to(DoseEventStatus.ALERTED)

    def mark_taken(self) -> None:
        self.transition_to(DoseEventStatus.TAKEN)

    def mark_pending(self) -> None:
        next_status = (
            DoseEventStatus.PENDING
            if self.status == DoseEventStatus.ALERTED
            else DoseEventStatus.ALERTED
        )
        self.transition_to(next_status)

    def mark_skipped(self) -> None:
        self.transition_to(DoseEventStatus.SKIPPED)
        self.confirmed_at = datetime.now(timezone.utc)

    def mark_synced(self) -> None:
        if self.status not in {
            DoseEventStatus.TAKEN,
            DoseEventStatus.SKIPPED,
            DoseEventStatus.PENDING,
        }:
            raise ValueError("only completed, skipped, or pending doses can be synchronized")
        self.sync_status = SyncStatus.SYNCED

    def mark_failed(self) -> None:
        self.sync_status = SyncStatus.FAILED

    def set_source(self, source: Source) -> None:
        self.source = source

    def is_synced(self) -> bool:
        return self.sync_status == SyncStatus.SYNCED

    def is_pending(self) -> bool:
        return self.status == DoseEventStatus.PENDING

    def is_taken(self) -> bool:
        return self.status == DoseEventStatus.TAKEN

    def is_skipped(self) -> bool:
        return self.status == DoseEventStatus.SKIPPED

    def is_scheduled(self) -> bool:
        return self.status == DoseEventStatus.SCHEDULED

    def is_alerted(self) -> bool:
        return self.status == DoseEventStatus.ALERTED
