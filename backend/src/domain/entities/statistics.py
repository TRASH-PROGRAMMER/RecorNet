from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# clase para representar estadísticas
@dataclass
class StatisticsSnapshot:
    id: Optional[str] = None
    user_id: str = ""
    period: str = "" # e.g., "2026-08"
    adherence_percentage: float = 0.0
    consecutive_days: int = 0
    total_doses: int = 0
    taken_doses: int = 0
    pending_doses: int = 0
    missed_doses: int = 0
    calculated_at: datetime = field(default_factory=datetime.utcnow) # Fecha de cálculo de estadísticas
