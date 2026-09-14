from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.user import User

class UserRepository(ABC): # Clase abstracta para representar repositorios de usuarios
    @abstractmethod 
    def save(self, user: User) -> User: # Método para guardar un usuario
        """Guarda un usuario"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]: # Método para obtener un usuario por ID
        """Obtiene un usuario por su ID"""
        raise NotImplementedError
    @abstractmethod 
    def get_by_email(self, email: str) -> Optional[User]: # Método para obtener un usuario por email
        """Obtiene un usuario por su email"""
        raise NotImplementedError
    @abstractmethod
    def update(self, user: User) -> User:  #Método para actualizar un usuario
        """Actualiza un usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, user_id: str) -> bool:  #Método para eliminar un usuario
        raise NotImplementedError
