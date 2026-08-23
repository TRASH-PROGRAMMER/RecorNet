from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum 
import uuid
import src.domain.value_objects.idempotency_key as IdempotencyKey
# clase para representar un evento de dosis
#enums para el estado
class DoseEventStatus(str, Enum):
    PENDING = "pending"
    TAKEN = "taken"
    SKIPPED = "skipped"
    SCHEDULED = "scheduled"
    ALERTED = "alerted"
    

#enum para el estado de sincronización
class SyncStatus(str, Enum):
    SYNCED = "synced"
    FAILED = "failed"
    PENDING = "pending"
    
# clase para representar la fuente del evento de dosis
class Source(str, Enum):
    CLIENT = "client"
    MOBILE = "mobile" 
    API = "api" 

@dataclass
class DoseEvent:
    id: Optional[str] = None
    treatment_id: str = ""
    schedule_id: str = ""
    idempotency_key: IdempotencyKey = "" # para evitar la creación de múltiples eventos de dosis para el mismo horario
    scheduled_at: datetime = field(default_factory=datetime.now) # YYYY-MM-DDTHH:MM:SSZ format
    status: DoseEventStatus = DoseEventStatus.SCHEDULED # pending, taken, missed
    sync_status: SyncStatus = SyncStatus.PENDING # synced, unsynced, failed
    confirmed_at: datetime = field(default_factory=datetime.now) # fecha de confirmación del evento de dosis  
    source: Source = Source.CLIENT # fuente del evento de dosis    
    # pyrefly: enable-type-checking
    def __post_init__(self): # post_init es un método que se ejecuta después de __init__
        if self.scheduled_at is None: # si la fecha programada es None
            self.scheduled_at = datetime.now() # se establece la fecha programada como la fecha actual
        if self.confirmed_at is None: # si la fecha de confirmación es None
            self.confirmed_at = datetime.now() # se establece la fecha de confirmación como la fecha actual
        if self.status is None: # si el estado es None
            self.status = DoseEventStatus.PENDING # se establece el estado como pendiente
        if self.sync_status is None: # si el estado de sincronización es None
            self.sync_status = SyncStatus.PENDING # se establece el estado de sincronización como pendiente
        if self.source is None: # si la fuente es None
            self.source = "" # se establece la fuente como vacía
        if self.idempotency_key is None: # si la clave de idempotencia es None
            self.idempotency_key = IdempotencyKey() # se establece la clave de idempotencia como una nueva instancia de IdempotencyKey
        if self.id is None: # si el id es None
            self.id = str(uuid.uuid4()) # se establece el id como un nuevo uuid

# Métodos para cambiar el estado del evento de dosis
    def mark_taken(self):
        if self.status == DoseEventStatus.PENDING or self.status == DoseEventStatus.SCHEDULED: # si el evento de dosis está pendiente o programado
            self.status = DoseEventStatus.TAKEN # se marca como tomado
            self.sync_status = SyncStatus.UNSYNCED # se marca como no sincronizado
            self.confirmed_at = datetime.now() # se actualiza la fecha de confirmación

    def mark_skipped(self):
        if self.status == DoseEventStatus.PENDING or self.status == DoseEventStatus.SCHEDULED: # si el evento de dosis está pendiente o programado
            self.status = DoseEventStatus.SKIPPED # se marca como saltado
            self.sync_status = SyncStatus.UNSYNCED # se marca como no sincronizado
            self.confirmed_at = datetime.now() # se actualiza la fecha de confirmación
        