from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Schedule:
    times: List[str] # ["08:00", "20:00"]
    days_of_week: List[int] # [0, 1, 2, 3, 4, 5, 6]
