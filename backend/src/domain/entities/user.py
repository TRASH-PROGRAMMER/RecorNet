from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# clase para representar un usuario
@dataclass
class User:
    id: Optional[str] = None
    email: str = ""
    password_hash: str = ""
    first_name: str = ""
    last_name: str = ""
    phone: Optional[str] = None
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
