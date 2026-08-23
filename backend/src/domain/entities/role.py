from dataclasses import dataclass
from typing import Optional
from enum import Enum

# roles que pueden existir en el sistema
class RoleType(str, Enum):
    PATIENT = "patient"
    CAREGIVER = "caregiver"
    ADMIN = "admin"
# clase para representar un rol
@dataclass
class Role:
    id: Optional[str] = None
    name: RoleType = RoleType.PATIENT
    


