from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class UserDevices:
    id: Optional[str] = None
    user_id: str = ""
    device_token: str = ""
    device_id : Optional[str] = None
    os: str = ""  # 'android' or 'ios' or 'web'  
    fcm_token: str = ""
    notifications_consent: bool = False
    last_used_at: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())