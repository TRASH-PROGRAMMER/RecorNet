from dataclasses import dataclass
from enum import Enum


class IntervalUnit(str, Enum):
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    WEEKS = "weeks"


@dataclass(frozen=True)
class Interval:
    """Cadencia positiva y explícita de un tratamiento o recordatorio."""

    value: int = 1
    unit: IntervalUnit = IntervalUnit.DAYS

    def __post_init__(self) -> None:
        if self.value <= 0:
            raise ValueError("interval value must be positive")
