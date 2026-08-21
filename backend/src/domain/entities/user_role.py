from dataclasses import dataclass
from typing import Optional
@dataclass
class UserRole:
    id: Optional[str] = None
    user_id: int = 0
    role_id: int = 0

    #cambia el rol del usuario
    def change_role(self, role_id: int):
        self.role_id = role_id