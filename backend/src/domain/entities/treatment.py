from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Optional

from src.domain.entities.reminder import ReminderSchedule
from src.domain.value_objects.dosage import Dosage
from src.domain.value_objects.Frequency import Frequency

# Estados del tratamiento
class TreatmentStatus(str, Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

# Clase para representar el tratamiento
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
    version: int = 0
    status: TreatmentStatus = TreatmentStatus.ACTIVE

# Metodos para cambiar el estado del tratamiento
    def change_status(self, status: TreatmentStatus) -> None:
        self.status = status
        if status == TreatmentStatus.CANCELLED:
            self.end_date = date.today()
            self.version += 1
        elif status == TreatmentStatus.ACTIVE:
            self.end_date = date.today()
            self.version += 1
        elif status == TreatmentStatus.PAUSED:
            self.end_date = date.today()
            self.version += 1
        elif status == TreatmentStatus.COMPLETED:
            self.end_date = date.today()
            self.version += 1

    # Validaciones
    def __post_init__(self) -> None:
        if self.end_date < self.start_date:
            raise ValueError("end_date must be greater than or equal to start_date")


    # Metodos para verificar el estado actual
    def is_active(self) -> bool:
        return self.status == TreatmentStatus.ACTIVE
    # Metodos para verificar si el tratamiento esta pausado
    def is_paused(self) -> bool:
        return self.status == TreatmentStatus.PAUSED
    
    # Metodos para verificar si el tratamiento esta completado
    def is_completed(self) -> bool:
        return self.status == TreatmentStatus.COMPLETED

    # Metodos para verificar si el tratamiento esta cancelado
    def is_cancelled(self) -> bool:
        return self.status == TreatmentStatus.CANCELLED
    

# Alias temporal para no romper referencias existentes durante la migración.
Treatments = Treatment
