from src.domain.repositories.care_relationship_repository import CareRelationshipRepository
from src.domain.exceptions.domain_exceptions import UnauthorizedAccess


class CareAuthorizationService:
    """Centraliza la autorización del cuidador sobre un adulto mayor."""

    def __init__(self, relationships: CareRelationshipRepository) -> None:
        self._relationships = relationships

    def ensure_can_act(
        self,
        caregiver_id: str,
        elderly_id: str,
        permission: str,
    ) -> None:
        if not self._relationships.can_act_on(caregiver_id, elderly_id, permission):
            raise UnauthorizedAccess(
                f"caregiver {caregiver_id} cannot perform {permission} for elderly {elderly_id}"
            )
