from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.treatment import Treatment

class TreatmentRepository(ABC): # Clase abstracta para representar repositorios de tratamientos
    @abstractmethod
    def save(self, treatment: Treatment) -> Treatment: # Método para guardar un tratamiento
        pass

    @abstractmethod
    def get_by_id(self, treatment_id: str) -> Optional[Treatment]: # Método para obtener un tratamiento por ID
        pass

    @abstractmethod
    def get_by_patient_id(self, patient_id: str) -> List[Treatment]: # Método para obtener un tratamiento por paciente ID
        pass
