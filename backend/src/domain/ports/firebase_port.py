from abc import ABC, abstractmethod
from typing import List

class FirebasePort(ABC):
    @abstractmethod
    def send_notification(self, token: str, title: str, body: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def send_multicast_notification(self, tokens: List[str], title: str, body: str) -> bool:
        raise NotImplementedError
