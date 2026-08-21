from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum

class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

# clase para representar un usuario
@dataclass
class User:
    id: Optional[str] = None
    name: str = ""
    email: str = ""
    password_hash: str = ""
    phone: Optional[str] = None
    is_active: bool = True
    status: Status = Status.ACTIVE
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    #cambia el estado del usuario
    def change_status(self, status: Status):
        self.status = status
    
