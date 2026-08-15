from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.user import User

class UserRepository(ABC): # Clase abstracta para representar repositorios de usuarios
    @abstractmethod
    def save(self, user: User) -> User: # Método para guardar un usuario
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]: # Método para obtener un usuario por ID
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]: # Método para obtener un usuario por email
        pass
