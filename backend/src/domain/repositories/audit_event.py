from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from src.domain.entities.audit_event import AuditEvent

# pyre-ignore [13]
#Clase para representar el repositorio de eventos de auditoría
class AuditEventRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar eventos de auditoría
    def save(self, audit_event: AuditEvent) -> AuditEvent:
        """Guarda un evento de auditoría"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, audit_event_id: str) -> Optional[AuditEvent]:
        """Obtiene un evento de auditoría por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[AuditEvent]:
        """Obtiene los eventos de auditoría de un usuario"""
        raise NotImplementedError
    @abstractmethod
    def get_for_patient(self, patient_id: str) -> List[AuditEvent]:
        """Obtiene los eventos de auditoría de un paciente"""
        raise NotImplementedError
    @abstractmethod
    def get_by_resource(self, resource_type: str, resource_id: str) -> List[AuditEvent]:
        """Obtiene los eventos de auditoría de un recurso"""
        raise NotImplementedError
    @abstractmethod
    def get_range_by_resource(self, resource_type: str, resource_id: str, start_date: datetime, end_date: datetime) -> List[AuditEvent]:
        """Obtiene los eventos de auditoría de un recurso en un rango de fechas"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, audit_event_id: str) -> bool:
        """Elimina un evento de auditoría"""
        raise NotImplementedError
    @abstractmethod
    def delete_old(self, days: int) -> int:
        """Elimina eventos de auditoría antiguos"""
        raise NotImplementedError    
