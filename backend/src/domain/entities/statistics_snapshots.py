from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
# clase para representar una instantánea de estadísticas
@dataclass
class StatisticsSnapshots:
    id: Optional[str] = None  # ID de la instantánea
    user_id: str = "" # ID del usuario
    snapshot: datetime = field(default_factory=datetime.utcnow)  # Fecha de la instantánea
    metrics: dict = field(default_factory=dict)  # Métricas de la instantánea