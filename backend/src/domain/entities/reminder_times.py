from dataclasses import dataclass
from typing import Optional
from src.domain.entities.reminder import ReminderSchedule

 # clase para representar los horarios de los recordatorios
@dataclass
class ReminderTimes:
    id: Optional[str] = None
    reminder_schedule: ReminderSchedule = None
    time_of_day: str = "" # HH:MM format
    # pyrefly: enable-type-checking
    def __post_init__(self):
        if self.time_of_day is None:
            self.time_of_day = "00:00"
