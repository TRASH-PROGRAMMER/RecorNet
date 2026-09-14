from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.profiles import Profile

# pyre-ignore [13]
# Clase para representar el repositorio de perfiles
class ProfileRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar perfiles
    def save(self, profile: Profile) -> Profile:
        """Guarda un perfil"""
        raise NotImplementedError
    # Metodos para obtener perfiles
    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[Profile]:
        """Obtiene un perfil por su ID"""
        raise NotImplementedError
    # Metodos para obtener perfiles
    @abstractmethod
    def get_for_user(self, user_id: str) -> Optional[Profile]:
        """Obtiene los perfiles de un usuario"""
        raise NotImplementedError
    # Metodos para eliminar perfiles
    @abstractmethod
    def delete(self, profile_id: str) -> bool:
        """Elimina un perfil"""
        raise NotImplementedError
    
