from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.reminder import Reminder
#Clase para representar el repositorio de recordatorios
class ReminderRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar, obtener, actualizar y eliminar recordatorios
    def save(self, reminder: Reminder) -> Reminder:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, reminder_id: str) -> Optional[Reminder]:
        raise NotImplementedError
    @abstractmethod
    def get_for_patient(self, patient_id: str) -> List[Reminder]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, reminder_id: str) -> bool:
        raise NotImplementedError
        