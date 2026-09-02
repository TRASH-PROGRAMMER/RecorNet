from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.dose_events import DoseEvent

class DoseEventRepository(ABC):
    @abstractmethod
    def save(self, dose_event: DoseEvent) -> DoseEvent:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, dose_event_id: str) -> Optional[DoseEvent]:
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[DoseEvent]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, dose_event_id: str) -> bool:
        raise NotImplementedError
