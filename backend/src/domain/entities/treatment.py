from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from src.domain.value_objects.dosage import Dosage

# clase para representar un tratamiento
@dataclass
class Treatment:
    id: Optional[str] = None
    medication_id: str = ""
    patient_user_id: str = ""
    created_by_user_id: str = ""
    dosage: Dosage = field(default_factory=lambda: Dosage(0, "")) # Dosis del medicamento
    frequency: str = ""
    start_date: datetime = field(default_factory=datetime.utcnow) # Fecha de inicio del tratamiento
    end_date: Optional[datetime] = None # Fecha de fin del tratamiento
    is_active: bool = True # Estado del tratamiento
