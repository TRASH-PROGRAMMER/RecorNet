from dataclasses import dataclass
# clase para representar una hora de recordatorio
@dataclass(frozen=True)
class ReminderTime:
    hour: int
    minute: int
    
    def __post_init__(self): # Método para validar la hora y minuto
        if not (0 <= self.hour <= 23):
            raise ValueError("Hour must be between 0 and 23") # Se valida que la hora esté en el rango correcto
        if not (0 <= self.minute <= 59):
            raise ValueError("Minute must be between 0 and 59") # Se valida que el minuto esté en el rango correcto
            
    def __str__(self): # Método para convertir la hora a string
        return f"{self.hour:02d}:{self.minute:02d}"
