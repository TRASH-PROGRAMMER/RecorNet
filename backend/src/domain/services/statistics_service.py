# pyrefly: ignore [missing-import]
from src.domain.repositories.reminder_repository import ReminderRepository

# pyre-ignore [13]
# Clase para representar el servicio de estadísticas
class StatisticsService:
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para obtener estadísticas
    def get_by_id(self, statistics_id: str) -> Optional[Statistics]:
        """Obtiene estadísticas por su ID"""
        raise NotImplementedError
    # Metodos para actualizar estadísticas
    @abstractmethod
    def update(self, statistics_id: str, statistics: Statistics) -> Optional[Statistics]:
        """Actualiza estadísticas"""
        raise NotImplementedError
    # Metodos para eliminar estadísticas
    @abstractmethod
    def delete(self, statistics_id: str) -> bool:
        """Elimina estadísticas"""
        raise NotImplementedError
    # Metodos para obtener estadísticas pendientes
    @abstractmethod
    def get_pending(self) -> List[Statistics]:
        """Obtiene las estadísticas pendientes"""
        raise NotImplementedError