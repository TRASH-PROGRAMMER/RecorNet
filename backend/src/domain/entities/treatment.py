from typing import Any
from dataclasses import dataclass, field
from datetime import date
from typing import Optional
from src.domain.value_objects.dosage import Dosage
from src.domain.value_objects.Frequency import Frequency
from src.domain.value_objects.schedule import Schedule
from enum import Enum
from src.domain.entities.medication import Medication
from src.domain.entities.user import User
# pyrefly: ignore [missing-import]
from src.domain.entities.reminder_schedule import ReminderSchedule

# clase para representar el estado del tratamiento
class TreatmentStatus(str,Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CANCELLED = "CANCELLED"


# clase para representar un tratamiento
@dataclass
class Treatments:
    id: Optional[str] = None
    medication_id: int = 0
    medications: list[Medication] = field(default_factory=list) 
    patient_user_id: int = 0
    users: Optional[User] = None
    created_by_user_id: int = 0 
    dosage: Dosage = field(default_factory=lambda: Dosage(0, "")) # Dosis del medicamento
    frequency: Frequency = field(default_factory=lambda: Frequency(0, "")) # Frecuencia del tratamiento
    schedules: list[Any] = field(default_factory=list) # Horario de las tomas
    start_date: date = field(default_factory=date.today) # Fecha de inicio del tratamiento
    end_date: date = field(default_factory=date.today) # Fecha de fin del tratamiento
    version: int = 1
    status: TreatmentStatus = TreatmentStatus.ACTIVE # Estado del tratamiento (ACTIVE, INACTIVE, CANCELLED)
    def change_status(self, status: TreatmentStatus):
        self.status = status
        self.version += 1

