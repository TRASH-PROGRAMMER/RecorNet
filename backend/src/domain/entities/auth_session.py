from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import uuid4


class AuthSessionStatus(str, Enum):
    ACTIVE = "active"
    REVOKED = "revoked"
    EXPIRED = "expired"


@dataclass
class AuthSession:
    """Sesión revocable de un usuario, asociable de forma opcional a un dispositivo."""

    user_id: str
    refresh_token_hash: str
    expires_at: datetime
    id: str = field(default_factory=lambda: str(uuid4()))
    device_id: Optional[str] = None
    status: AuthSessionStatus = AuthSessionStatus.ACTIVE
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    revoked_at: Optional[datetime] = None

    def revoke(self, at: Optional[datetime] = None) -> None:
        self.status = AuthSessionStatus.REVOKED
        self.revoked_at = at or datetime.now(timezone.utc)

    def is_active(self, now: Optional[datetime] = None) -> bool:
        reference = now or datetime.now(timezone.utc)
        return self.status == AuthSessionStatus.ACTIVE and self.expires_at > reference
