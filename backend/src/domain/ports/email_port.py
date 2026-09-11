from abc import ABC, abstractmethod

class EmailPort(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        raise NotImplementedError
