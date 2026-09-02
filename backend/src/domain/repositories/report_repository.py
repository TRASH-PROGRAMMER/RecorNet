from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.reports import Report

class ReportRepository(ABC):
    @abstractmethod
    def save(self, report: Report) -> Report:
        raise NotImplementedError
    @abstractmethod
    def get_by_id(self, report_id: str) -> Optional[Report]:
        raise NotImplementedError
    @abstractmethod
    def get_for_user(self, user_id: str) -> List[Report]:
        raise NotImplementedError
    @abstractmethod
    def delete(self, report_id: str) -> bool:
        raise NotImplementedError