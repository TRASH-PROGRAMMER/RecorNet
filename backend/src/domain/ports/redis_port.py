from abc import ABC, abstractmethod

class RedisPort(ABC):
    @abstractmethod
    def get(self, key: str) -> str:
        raise NotImplementedError
    @abstractmethod
    def set(self, key: str, value: str, ex: int) -> bool:
        """Establece una clave con un valor y un tiempo de expiración"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, key: str) -> bool:
        """Elimina una clave"""
        raise NotImplementedError
