from dataclasses import dataclass
# Clase abstracta para representar una dosis
@dataclass(frozen=True)
class Dosage:
    amount: float
    unit: str # e.g., "mg", "ml", "pastilla(s)"
