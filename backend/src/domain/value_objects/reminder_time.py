from dataclasses import dataclass

@dataclass(frozen=True)
class ReminderTime:
    hour: int
    minute: int
    
    def __post_init__(self):
        if not (0 <= self.hour <= 23):
            raise ValueError("Hour must be between 0 and 23")
        if not (0 <= self.minute <= 59):
            raise ValueError("Minute must be between 0 and 59")
            
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"
