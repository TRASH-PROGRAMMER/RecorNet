from dataclasses import dataclass, field
from typing import Optional
from src.domain.entities.user import User
# clase para representar una relación de cuidado
from enum import Enum 

class status(str,Enum): 
    ACTIVE = "active" 
    INACTIVE = "inactive" 
    CANCELLED = "cancelled"  
    PENDING = "pending"    

@dataclass
class CareRelationship:
    id: Optional[str] = None
    caregiver_id: str = "" 
    elderly_id: str = "" 
    permissions: dict = field(default_factory=dict) # permisos del cuidador
    status: status = status.ACTIVE # estado de la relación

    def add_permission(self, permission: str):
        self.permissions[permission] = True

    def remove_permission(self, permission: str):
        self.permissions.pop(permission, None) # remueve el permiso

    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions # verifica si tiene el permiso

    def update_status(self, status: str):
        self.status = status # actualiza el estado

    def is_active(self) -> bool:
        return self.status == "active" # verifica si la relación está activa

    def is_owner(self, user: User) -> bool:
        return self.elderly_id == user.id # verifica si el usuario es el dueño

    def is_caregiver(self, user: User) -> bool:
        return self.caregiver_id == user.id # verifica si el usuario es el cuidador
    
