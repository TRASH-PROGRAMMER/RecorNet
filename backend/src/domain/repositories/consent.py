from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from src.domain.entities.consent import Consent

class ConsentRepository(ABC):
    @abstractmethod
    def save(self, consent: Consent) -> Consent:
        """Guarda un consentimiento"""
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, consent_id: str) -> Optional[Consent]:
        """Obtiene un consentimiento por su ID"""
        raise NotImplementedError
    @abstractmethod
    def get_by_elderly(self, elderly_id: str) -> List[Consent]:
        """Obtiene los consentimientos de un adulto mayor"""
        raise NotImplementedError
    @abstractmethod
    def delete(self, consent_id: str) -> bool:
        """Elimina un consentimiento"""
        raise NotImplementedError