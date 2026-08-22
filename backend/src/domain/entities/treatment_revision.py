from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class TreatmentRevision:
    """Versión auditable de un tratamiento para sincronizar cambios y resolver conflictos."""

    treatment_id: str
    version: int
    changed_by_user_id: str
    changes: dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def validate(self) -> None:
        if self.version <= 0:
            raise ValueError("treatment revision version must be positive")
