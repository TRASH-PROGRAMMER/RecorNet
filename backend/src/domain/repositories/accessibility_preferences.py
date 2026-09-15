from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.accessibility_preferences import AccessibilityPreferences

# pyre-ignore [13]
# Clase para representar el repositorio de preferencias de accesibilidad
class AccessibilityPreferencesRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar preferencias de accesibilidad
    def save(self, accessibility_preferences: AccessibilityPreferences) -> AccessibilityPreferences:
        """Guarda una preferencia de accesibilidad"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, accessibility_preferences_id: str) -> Optional[AccessibilityPreferences]:
        """Obtiene una preferencia de accesibilidad por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_elderly(self, elderly_id: str) -> List[AccessibilityPreferences]:
        """Obtiene las preferencias de accesibilidad de un adulto mayor"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, accessibility_preferences_id: str) -> bool:
        """Elimina una preferencia de accesibilidad"""
        raise NotImplementedError