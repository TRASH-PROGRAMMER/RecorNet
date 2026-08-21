from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum
# estado del medicamento
class MedicationStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    CANCELLED = "cancelled"
    PENDING = "pending"

# clase para representar un medicamento
@dataclass
class Medication:
    id: Optional[str] = None
    name: str = ""
    description: Optional[str] = None
    photo_url: Optional[str] = None
    form: str = ""
    manufacturer: str = ""
    created_by_user_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow) # Fecha de creación del medicamento
    status: MedicationStatus = MedicationStatus.ACTIVE
