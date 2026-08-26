from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional

from src.domain.entities.reminder import ReminderSchedule
from src.domain.value_objects.dosage import Dosage
from src.domain.value_objects.Frequency import Frequency


class TreatmentStatus(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Treatment:
    id: Optional[str] = None
    medication_id: int = 0
    patient_user_id: int = 0
    created_by_user_id: int = 0
    dosage: Dosage = field(default_factory=lambda: Dosage(0, ""))
    instructions: str = ""
    frequency: Frequency = field(default_factory=Frequency)
    schedules: list[ReminderSchedule] = field(default_factory=list)
    start_date: date = field(default_factory=date.today)
    end_date: date = field(default_factory=date.today)
    version: int = 1
    status: TreatmentStatus = TreatmentStatus.ACTIVE

    def change_status(self, status: TreatmentStatus) -> None:
        self.status = status
        self.version += 1
        if status == TreatmentStatus.CANCELLED:
            self.end_date = date.today()

    def __post_init__(self) -> None:
        if self.end_date < self.start_date:
            raise ValueError("end_date must be greater than or equal to start_date")

    def update_start_date(self, start_date: date) -> None:
        if start_date > self.end_date:
            raise ValueError("start_date must be less than or equal to end_date")
        self.start_date = start_date
        self.version += 1


# Alias temporal para no romper referencias existentes durante la migración.
Treatments = Treatment
