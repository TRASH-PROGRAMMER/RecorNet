from dataclasses import dataclass
from typing import Optional, List

# clase para representar un recordatorio
@dataclass
class ReminderSchedule:
    id: Optional[str] = None
    treatment_id: str = ""
    scheduled_time: str = "" # HH:MM format
    days_of_week: List[int] = None # 0 = Monday, 6 = Sunday
    is_active: bool = True

    def __post_init__(self):  # método que se ejecuta después de la inicialización
        if self.days_of_week is None: # si no se especifica ningún día de la semana
            self.days_of_week = [0, 1, 2, 3, 4, 5, 6] # se especifica todos los días de la semana
