from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.role import Role

# pyre-ignore [13]
# Clase para representar el repositorio de roles
class RoleRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar roles
    def save(self, role: Role) -> Role:
        """Guarda un rol"""
        raise NotImplementedError
    # Metodos para obtener roles
    @abstractmethod
    def get_by_id(self, role_id: str) -> Optional[Role]:
        """Obtiene un rol por su ID"""
        raise NotImplementedError
    # Metodos para obtener roles
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[Role]:
        """Obtiene los roles de un usuario"""
        raise NotImplementedError
    # Metodos para eliminar roles
    @abstractmethod
    def delete(self, role_id: str) -> bool:
        """Elimina un rol"""
        raise NotImplementedError
    