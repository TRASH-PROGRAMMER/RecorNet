from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.reminder_times import ReminderTimes

# pyre-ignore [13]
# Clase para representar el repositorio de tiempos de remedios
class ReminderTimesRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar tiempos de remedios
    def save(self, reminder_times: ReminderTimes) -> ReminderTimes:
        """Guarda un tiempo de remedio"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, reminder_times_id: str) -> Optional[ReminderTimes]:
        """Obtiene un tiempo de remedio por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_remedy(self, remedy_id: str) -> List[ReminderTimes]:
        """Obtiene los tiempos de remedios de un remedio"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[ReminderTimes]:
        """Obtiene los tiempos de remedios de un usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, remedy_times_id: str) -> bool:
        """Elimina un tiempo de remedio"""
        raise NotImplementedError