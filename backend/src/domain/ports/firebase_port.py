from abc import ABC, abstractmethod
from typing import List
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

class FirebasePort(ABC):
    @abstractmethod
    def send_notification(self, token: str, title: str, body: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def send_multicast_notification(self, tokens: List[str], title: str, body: str) -> bool:
        raise NotImplementedError

class FirebaseConnection:
    def __init__(self):
        self.cred = credentials.Certificate("path/to/serviceAccountKey.json")
        self.app = firebase_admin.initialize_app(self.cred)
    def send_notification(self, token: str, title: str, body: str) -> bool:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
        )
        response = messaging.send(message)
        return True
    def send_multicast_notification(self, tokens: List[str], title: str, body: str) -> bool:
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            tokens=tokens,
        )
        response = messaging.send_multicast(message)
        return True 