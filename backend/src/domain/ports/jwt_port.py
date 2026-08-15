from abc import ABC, abstractmethod

class JwtPort(ABC): # Clase abstracta para representar puertos de JWT
    @abstractmethod
    def generate_token(self, payload: dict, expiration_minutes: int) -> str: # Método para generar un token JWT
        
    @abstractmethod
    def decode_token(self, token: str) -> dict:
        pass
