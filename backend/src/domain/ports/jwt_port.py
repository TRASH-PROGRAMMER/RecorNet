from abc import ABC, abstractmethod
import jwt

class JwtPort(ABC): # Clase abstracta para representar puertos de JWT
    @abstractmethod
    def generate_token(self, payload: dict, expiration_minutes: int) -> str: # Método para generar un token JWT
        pass
        
    @abstractmethod
    def decode_token(self, token: str) -> dict: # Método para decodificar un token JWT
        pass

class JwtConnection:
    def __init__(self):
        self.jwt_client = jwt
    def generate_token(self, payload: dict, expiration_minutes: int) -> str:
        return self.jwt_client.encode(payload, "secret", algorithm="HS256")
    def decode_token(self, token: str) -> dict:
        return self.jwt_client.decode(token, "secret", algorithms=["HS256"])
