# pyrefly: ignore [missing-import]
from src.domain.repositories.reminder_repository import ReminderRepository

# pyre-ignore [13]
# Clase para representar el servicio de recordatorio
class ReminderService:
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar recordatorios
    def save(self, reminder: Reminder) -> Reminder:
        """Guarda un recordatorio"""
        raise NotImplementedError
    # Metodos para obtener recordatorios
    @abstractmethod
    def get_by_id(self, reminder_id: str) -> Optional[Reminder]:
        """Obtiene un recordatorio por su ID"""
        raise NotImplementedError
    # Metodos para actualizar recordatorios
    @abstractmethod
    def update(self, reminder_id: str, reminder: Reminder) -> Optional[Reminder]:
        """Actualiza un recordatorio"""
        raise NotImplementedError
    # Metodos para eliminar recordatorios
    @abstractmethod
    def delete(self, reminder_id: str) -> bool:
        """Elimina un recordatorio"""
        raise NotImplementedError
    # Metodos para obtener recordatorios pendientes
    @abstractmethod
    def get_pending(self) -> List[Reminder]:
        """Obtiene los recordatorios pendientes"""
        raise NotImplementedError