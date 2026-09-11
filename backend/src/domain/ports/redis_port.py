from abc import ABC, abstractmethod
import redis
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

class RedisConnection: 
    def __init__(self):
        self.redis_client = redis.Redis(
            host='localhost',
            port=6379,
            decode_responses=True
        )
    def get(self, key: str) -> str:
        return self.redis_client.get(key)
    def set(self, key: str, value: str, ex: int) -> bool:
        return self.redis_client.set(key, value, ex)
    def delete(self, key: str) -> bool:
        return self.redis_client.delete(key)