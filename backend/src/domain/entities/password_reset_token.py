from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4


@dataclass
class PasswordResetToken:
    """Token de recuperación almacenado como hash y consumible una sola vez."""

    user_id: str
    token_hash: str
    expires_at: datetime
    id: str = field(default_factory=lambda: str(uuid4()))
    used_at: Optional[datetime] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def consume(self, at: Optional[datetime] = None) -> None:
        if self.used_at is not None:
            raise ValueError("password reset token has already been consumed")
        self.used_at = at or datetime.now(timezone.utc)

    def is_valid(self, now: Optional[datetime] = None) -> bool:
        reference = now or datetime.now(timezone.utc)
        return self.used_at is None and self.expires_at > reference
