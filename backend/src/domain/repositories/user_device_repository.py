from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.user_devices import UserDevices

class UserDeviceRepository(ABC):
    """Repositorio de dispositivos de usuarios"""
    @abstractmethod
    def save(self, user_device: UserDevices) -> UserDevices:
        """Guarda un dispositivo de usuario"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, user_device_id: str) -> Optional[UserDevices]:
        """Obtiene un dispositivo de usuario por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_by_device(self, user_id: str, device_id: str) -> Optional[UserDevices]:
        """Obtiene un dispositivo de usuario por su ID y el ID del dispositivo"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[UserDevices]:
        """Obtiene los dispositivos de un usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, user_device_id: str) -> bool:
        """Elimina un dispositivo"""
        raise NotImplementedError