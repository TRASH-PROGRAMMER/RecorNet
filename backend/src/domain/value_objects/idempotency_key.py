from dataclasses import dataclass, field
import uuid

# clase para representar una clave de idempotencia
@dataclass(frozen=True)
class IdempotencyKey:
    key: str = field(default_factory=lambda: str(uuid.uuid4()))