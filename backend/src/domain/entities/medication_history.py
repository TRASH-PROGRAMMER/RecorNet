from dataclasses import dataclass
from datetime import datetime
from typing import Optional

# clase para registrar los eventos de dosis
@dataclass
class DoseEvent: 
    id: Optional[str] = None
    reminder_schedule_id: str = ""
    treatment_id: str = ""
    user_id: str = ""
    scheduled_at: datetime = None
    taken_at: Optional[datetime] = None
    status: str = "PROGRAMADA" # PROGRAMADA, ALERTADA, TOMADA, PENDIENTE, OMITIDA, SINCRONIZADA
