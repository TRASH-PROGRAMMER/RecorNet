from dataclasses import dataclass

@dataclass(frozen=True)
class Dosage:
    amount: float
    unit: str # e.g., "mg", "ml", "pastilla(s)"
