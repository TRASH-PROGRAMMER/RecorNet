from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.care_relationship import CareRelationship


class CareRelationshipRepository(ABC):
    """Puerto de lectura de relaciones de cuidado autorizadas."""

    @abstractmethod
    def get_between(self, caregiver_id: str, elderly_id: str) -> Optional[CareRelationship]:
        """Obtiene la relación vigente, si existe."""
        raise NotImplementedError

    def can_act_on(self, caregiver_id: str, elderly_id: str, permission: str) -> bool:
        relationship = self.get_between(caregiver_id, elderly_id)
        return bool(
            relationship
            and relationship.is_active()
            and relationship.has_permission(permission)
        )
