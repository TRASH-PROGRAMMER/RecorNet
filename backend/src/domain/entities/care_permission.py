from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import uuid4


class CarePermissionCode(str, Enum):
    VIEW_TREATMENTS = "view_treatments"
    MANAGE_TREATMENTS = "manage_treatments"
    VIEW_HISTORY = "view_history"
    VIEW_STATISTICS = "view_statistics"
    RECEIVE_ESCALATIONS = "receive_escalations"


@dataclass
class CarePermission:
    """Permiso individual otorgado dentro de una relación cuidador-adulto mayor."""

    care_relationship_id: str
    code: CarePermissionCode
    id: str = field(default_factory=lambda: str(uuid4()))
    granted_by_user_id: Optional[str] = None
    granted_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    revoked_at: Optional[datetime] = None

    @property
    def is_active(self) -> bool:
        return self.revoked_at is None

    def revoke(self, at: Optional[datetime] = None) -> None:
        self.revoked_at = at or datetime.now(timezone.utc)
