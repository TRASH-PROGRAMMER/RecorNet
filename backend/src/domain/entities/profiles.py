from dataclasses import dataclass, field
from typing import Optional

# clase para representar un perfil
@dataclass
class Profile:
    id: Optional[str] = None
    user_id: int = 0
    avatar_url: Optional[str] = None
    preferences: dict = field(default_factory=dict)
    