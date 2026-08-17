from dataclasses import dataclass
from src.domain.value_objects.interval import Interval
# clase para representar la frecuencia del tratamiento
@dataclass
class Frequency:
    interval: Interval = field(default_factory=lambda: Interval(0, "")) # Intervalo de las tomas