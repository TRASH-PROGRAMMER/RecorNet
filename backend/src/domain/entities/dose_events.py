from dataclasses import dataclass, field
from typing import Optional
from enum import Enum 
# clase para representar un evento de dosis
@dataclass
class DoseEvent:
    id: Optional[str] = None
    treatment_id: str = ""
    reminder_id: str = ""
    dose_time: str = "" # HH:MM format
    dose_date: str = "" # YYYY-MM-DD format
    status: str = "" # pending, taken, missed
    created_at: str = "" # YYYY-MM-DD HH:MM:SS format
    updated_at: str = "" # YYYY-MM-DD HH:MM:SS format
    # pyrefly: enable-type-checking
    def __post_init__(self):
        if self.dose_time is None:
            self.dose_time = "00:00"
        if self.dose_date is None:
            self.dose_date = "2022-01-01"
        if self.status is None:
            self.status = "pending"
        if self.created_at is None:
            self.created_at = "2022-01-01 00:00:00"
        if self.updated_at is None:
            self.updated_at = "2022-01-01 00:00:00"