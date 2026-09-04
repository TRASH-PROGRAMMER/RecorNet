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
        raise NotImplementedError
    @abstractmethod
    def get_for_patient(self, patient_id: str) -> List[Report]:
        raise NotImplementedError
    @abstractmethod
    def get_for_caregiver(self, caregiver_id: str) -> List[Report]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, report_id: str) -> bool:
        raise NotImplementedError