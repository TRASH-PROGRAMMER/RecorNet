from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.treatment_revision import TreatmentRevision

# pyre-ignore [13]
# Clase para representar el repositorio de revisiones de tratamiento
class TreatmentRevisionRepository(ABC):
    #@abstractmethod indica que el metodo es abstracto y debe ser implementado por la clase hija
    @abstractmethod
    # Metodos para guardar revisiones de tratamiento
    def save(self, treatment_revision: TreatmentRevision) -> TreatmentRevision:
        """Guarda una revisión de tratamiento"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, treatment_revision_id: str) -> Optional[TreatmentRevision]:
        """Obtiene una revisión de tratamiento por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_for_treatment(self, treatment_id: str) -> List[TreatmentRevision]:
        """Obtiene las revisiones de tratamiento de un tratamiento"""
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[TreatmentRevision]:
        """Obtiene las revisiones de tratamiento de un usuario"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, treatment_revision_id: str) -> bool:
        """Elimina una revisión de tratamiento"""
        raise NotImplementedError    