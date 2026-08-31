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

    # Validaciones
    def __post_init__(self) -> None:
        if self.end_date < self.start_date:
            raise ValueError("end_date must be greater than or equal to start_date")

    # Metodos para actualizar el tratamiento
    def update_start_date(self, start_date: date) -> None:
        if start_date > self.end_date:
            raise ValueError("start_date must be less than or equal to end_date")
        self.start_date = start_date
        self.version += 1
    # Metodos para actualizar los horarios
    def updated_schedule(self, schedules: list[ReminderSchedule]) -> None:
        self.schedules = schedules
        self.version += 1
    # Metodos para actualizar la dosis
    def updated_dosage(self, dosage: Dosage) -> None:
        self.dosage = dosage
        self.version += 1
    # Metodos para actualizar la frecuencia
    def updated_frequency(self, frequency: Frequency) -> None:
        self.frequency = frequency
        self.version += 1
    # Metodos para actualizar las instrucciones
    def updated_instructions(self, instructions: str) -> None:
        self.instructions = instructions
        self.version += 1
    
    # Metodos para actualizar el estado
    def updated_status(self, status: TreatmentStatus) -> None:
        self.status = status
        self.version += 1
    # Metodos para actualizar la fecha de fin
    def updated_end_date(self, end_date: date) -> None:
        self.end_date = end_date
        self.version += 1

    # Metodos para verificar el estado
    def is_active(self) -> bool:
        return self.status == TreatmentStatus.ACTIVE
        
    # Metodos para verificar el estado
    def is_paused(self) -> bool:
        return self.status == TreatmentStatus.PAUSED
    
    # Metodos para verificar el estado
    def is_completed(self) -> bool:
        return self.status == TreatmentStatus.COMPLETED
        
    # Metodos para verificar el estado
    def is_cancelled(self) -> bool:
        return self.status == TreatmentStatus.CANCELLED
    

# Alias temporal para no romper referencias existentes durante la migración.
Treatments = Treatment
