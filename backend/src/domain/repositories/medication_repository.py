from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.entities.medication import Medication

class MedicationRepository(ABC): # Clase abstracta para representar repositorios de medicamentos
    @abstractmethod
    def save(self, medication: Medication) -> Medication: # Método para guardar un medicamento
        pass

    @abstractmethod
    def get_by_id(self, medication_id: str) -> Optional[Medication]: # Método para obtener un medicamento por ID
        pass

    @abstractmethod
    def get_by_caregiver_id(self, caregiver_id: str) -> List[Medication]: # Método para obtener un medicamento por caregiver ID
        pass
        
    @abstractmethod
    def delete(self, medication_id: str) -> bool: # Método para eliminar un medicamento
        pass
