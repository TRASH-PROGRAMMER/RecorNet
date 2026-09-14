from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.reports import Report
#Clase para representar el repositorio de reportes
class ReportRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar, obtener, actualizar y eliminar reportes
    def save(self, report: Report) -> Report:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, report_id : str) -> Optional[Report]:
        """Guarda un reporte"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, report_id : str) -> Optional[Report]:
        """Obtiene un reporte por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_by_subject(self, subject_id: str) -> List[Report]:
        """Obtiene un reporte por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_by_creator(self, created_by_user_id: str) -> List[Report]:
        """Obtiene los reportes creados por un usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, report_id: str) -> bool:
        """Elimina un reporte"""
        raise NotImplementedError