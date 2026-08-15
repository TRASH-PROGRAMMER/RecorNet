from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class MedicationImage:
    url: str
    public_id: Optional[str] = None
