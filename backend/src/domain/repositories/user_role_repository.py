from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.user_role import UserRole

# pyre-ignore [13]
# Clase para representar el repositorio de roles de usuario
class UserRoleRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar roles de usuario
    def save(self, user_role: UserRole) -> UserRole:
        raise NotImplementedError
    # Metodos para obtener roles de usuario
    @abstractmethod
    def get_by_id(self, user_role_id: str) -> Optional[UserRole]:
        raise NotImplementedError
    # Metodos para obtener roles de usuario
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[UserRole]:
        raise NotImplementedError
    # Metodos para eliminar roles de usuario
    @abstractmethod
    def delete(self, user_role_id: str) -> bool:
        raise NotImplementedError
    
