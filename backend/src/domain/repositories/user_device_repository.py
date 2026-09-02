from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.user_devices import UserDevice

class UserDeviceRepository(ABC):
    @abstractmethod
    def save(self, user_device: UserDevice) -> UserDevice:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, user_device_id: str) -> Optional[UserDevice]:
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[UserDevice]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, user_device_id: str) -> bool:
        raise NotImplementedError