
from abc import ABC, abstractmethod


class EmailPort(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        raise NotImplementedError
    @abstractmethod
    def send_password_reset(self, to: str, token: str) -> bool:
        raise NotImplementedError


