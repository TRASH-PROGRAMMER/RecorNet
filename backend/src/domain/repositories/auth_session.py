from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.auth_session import AuthSession

class AuthSessionRepository(ABC):
    """Repositorio de sesiones de autenticación"""
    @abstractmethod
    def save(self, session: AuthSession) -> AuthSession:
        """Guarda una sesión de autenticación"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, session_id: str) -> Optional[AuthSession]:
        """Obtiene una sesión de autenticación por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_active_for_user(self, user_id: str) -> List[AuthSession]:
        """Obtiene las sesiones activas para un usuario"""
        raise NotImplementedError
    @abstractmethod
    def revoke(self, session_id: str) -> bool:
        """Revoca una sesión de autenticación"""
        raise NotImplementedError