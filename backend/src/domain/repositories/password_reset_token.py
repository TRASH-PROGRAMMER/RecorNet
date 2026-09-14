from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.password_reset_token import PasswordResetToken

class PasswordResetTokenRepository(ABC):
    """Repositorio de tokens de restablecimiento de contraseña"""
    @abstractmethod
    def save(self, token: PasswordResetToken) -> PasswordResetToken:
        """Guarda un token de restablecimiento de contraseña"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, token_id: str) -> Optional[PasswordResetToken]:
        """Obtiene un token de restablecimiento de contraseña por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_by_user(self, user_id: str) -> Optional[PasswordResetToken]:
        """Obtiene un token de restablecimiento de contraseña por su usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, token_id: str) -> bool:
        """Elimina un token de restablecimiento de contraseña"""
        raise NotImplementedError
