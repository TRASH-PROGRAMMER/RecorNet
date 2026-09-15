from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.care_permission import CarePermission

# pyre-ignore [13]
# Clase para representar el repositorio de permisos de cuidado
class CarePermissionRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar permisos de cuidado
    def save(self, care_permission: CarePermission) -> CarePermission:
        """Guarda un permiso de cuidado"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, care_permission_id: str) -> Optional[CarePermission]:
        """Obtiene un permiso de cuidado por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_caregiver(self, caregiver_id: str) -> List[CarePermission]:
        """Obtiene los permisos de cuidado de un cuidador"""
        raise NotImplementedError
    @abstractmethod
    def get_for_elderly(self, elderly_id: str) -> List[CarePermission]:
        """Obtiene los permisos de cuidado de un adulto mayor"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, care_permission_id: str) -> bool:
        """Elimina un permiso de cuidado"""
        raise NotImplementedError    