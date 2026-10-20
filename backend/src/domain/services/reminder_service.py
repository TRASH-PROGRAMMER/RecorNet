from abc import ABC, abstractmethod
from typing import Optional, List

# pyrefly: ignore [missing-import]
from src.domain.entities.reminder import ReminderSchedule
from src.domain.repositories.reminder_repository import ReminderRepository


# pyre-ignore [13]
# Clase para representar el servicio de recordatorio
class ReminderService(ABC):
    def __init__(self, reminder_repository: ReminderRepository) -> None:
        self._reminder_repository = reminder_repository
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar recordatorios
    def save(self, reminder: ReminderSchedule) -> ReminderSchedule:
        """Guarda un recordatorio"""
        raise NotImplementedError
    # Metodos para obtener recordatorios
    @abstractmethod
    def get_by_id(self, reminder_id: str) -> Optional[ReminderSchedule]:
        """Obtiene un recordatorio por su ID"""
        raise NotImplementedError
    # Metodos para actualizar recordatorios
    @abstractmethod
    def update(self, reminder_id: str, reminder: ReminderSchedule) -> Optional[ReminderSchedule]:
        """Actualiza un recordatorio"""
        raise NotImplementedError
    # Metodos para eliminar recordatorios
    @abstractmethod
    def delete(self, reminder_id: str) -> bool:
        """Elimina un recordatorio"""
        raise NotImplementedError
    # Metodos para obtener recordatorios pendientes
    @abstractmethod
    def get_pending(self) -> List[ReminderSchedule]:
        """Obtiene los recordatorios pendientes"""
        raise NotImplementedError
