from dataclasses import dataclass, field
from typing import List
from src.domain.entities.user import User

# es una clase que hereda de User  
@dataclass
class Elderly(User): 
    linked_caregivers: List['Caregiver'] = field(default_factory=list)  # lista de cuidadores
