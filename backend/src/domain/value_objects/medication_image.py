from dataclasses import dataclass
from typing import Optional

# Clase abstracta para representar una imagen de medicamento
@dataclass(frozen=True)
class MedicationImage:
    url: str
    public_id: Optional[str] = None
