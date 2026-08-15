from dataclasses import dataclass, field
from typing import List
from src.domain.entities.user import User
from src.domain.entities.elderly import Elderly


# es una clase que hereda de User 
@dataclass
class Caregiver(User):
    linked_elderlies: List[Elderly] = field(default_factory=list)  # lista de adultos mayores
    
