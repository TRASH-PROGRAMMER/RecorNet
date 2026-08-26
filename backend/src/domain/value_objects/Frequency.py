from dataclasses import dataclass, field

from src.domain.value_objects.interval import Interval
# clase para representar la frecuencia del tratamiento
@dataclass
class Frequency:
    interval: Interval = field(default_factory=Interval)
