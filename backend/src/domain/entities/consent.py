from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from uuid import uuid4


class ConsentType(str, Enum):
    DATA_PROCESSING = "data_processing"
    NOTIFICATIONS = "notifications"
    VOICE_GUIDANCE = "voice_guidance"


class ConsentStatus(str, Enum):
    GRANTED = "granted"
    REVOKED = "revoked"


@dataclass
class Consent:
    """Evidencia de la decisión de consentimiento del usuario y de su revocación."""

    user_id: str
    type: ConsentType
    id: str = field(default_factory=lambda: str(uuid4()))
    status: ConsentStatus = ConsentStatus.GRANTED
    device_id: Optional[str] = None
    policy_version: Optional[str] = None
    granted_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    revoked_at: Optional[datetime] = None

    def revoke(self, at: Optional[datetime] = None) -> None:
        self.status = ConsentStatus.REVOKED
        self.revoked_at = at or datetime.now(timezone.utc)
