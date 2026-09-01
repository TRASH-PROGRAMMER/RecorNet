from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
from enum import Enum

# clase para representar el estado del usuario
class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"


# Alias temporal para no romper importaciones existentes durante la migración.
Status = UserStatus

# clase para representar un usuario
@dataclass
class User:
    id: Optional[str] = None
    name: str = ""
    email: str = ""
    password_hash: str = ""
    phone: Optional[str] = None
    status: UserStatus = UserStatus.ACTIVE
    deleted_at: Optional[datetime] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    # se agregan propiedades y metodos para manejar el estado del usuario
    @property
    def is_active(self) -> bool:
        return self.status == UserStatus.ACTIVE
# metodo para cambiar el estado del usuario
    def change_status(self, status: UserStatus) -> None:
        self.status = status
        self.updated_at = datetime.now(timezone.utc)
# metodo para eliminar un usuario
    def soft_delete(self) -> None:
        self.status = UserStatus.DELETED
        self.deleted_at = datetime.now(timezone.utc)
        self.updated_at = self.deleted_at
