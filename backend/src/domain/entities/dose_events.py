from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum 
import uuid
# clase para representar un evento de dosis
#enums para el estado
class DoseEventStatus(str, Enum):
    PENDING = "pending"
    TAKEN = "taken"
    SKIPPED = "skipped"
    SCHEDULED = "scheduled"
    ALERTED = "alerted"
    FAILED = "failed"
    SYNCED = "synced"
    

#enum para el estado de sincronización
class SyncStatus(str, Enum):
    SYNCED = "synced"
    UNSYNCED = "unsynced"
    FAILED = "failed"
    
# clase para representar la fuente del evento de dosis
class Source(str, Enum):
    WEB = "web"
    MOBILE = "mobile" 
    API = "api" 

@dataclass
class DoseEvent:
    id: Optional[str] = None
    treatment_id: str = ""
    schedule_id: str = ""
    indepotency_key: str = "" # para evitar la creación de múltiples eventos de dosis para el mismo horario
    scheduled_at: datetime = field(default_factory=datetime.now) # YYYY-MM-DDTHH:MM:SSZ format
    status: DoseEventStatus = DoseEventStatus.PENDING # pending, taken, missed
    sync_status: SyncStatus = SyncStatus.UNSYNCED # synced, unsynced, failed
    confirmed_at: datetime = field(default_factory=datetime.now) # fecha de confirmación del evento de dosis  
    source: Source = Source.WEB # fuente del evento de dosis    
    # pyrefly: enable-type-checking
    def __post_init__(self):
        if self.scheduled_at is None:
            self.scheduled_at = datetime.now()
        if self.confirmed_at is None:
            self.confirmed_at = datetime.now()
        if self.status is None:
            self.status = DoseEventStatus.PENDING
        if self.sync_status is None:
            self.sync_status = SyncStatus.UNSYNCED
        if self.source is None:
            self.source = ""
        if self.indepotency_key is None:
            self.indepotency_key = ""
        if self.id is None:
            self.id = str(uuid.uuid4())