from dataclasses import dataclass

# clase para representar una clave de idempotencia
@dataclass(frozen=True)
class IdempotencyKey:
    key: str