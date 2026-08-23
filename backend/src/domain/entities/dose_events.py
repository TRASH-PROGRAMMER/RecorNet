from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum 
import uuid
from src.domain.value_objects.idempotency_key import IdempotencyKey
# clase para representar un evento de dosis
#enums para el estado
class DoseEventStatus(str, Enum):
    PENDING = "pending" #
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
    idempotency_key: IdempotencyKey = field(default_factory=IdempotencyKey) # para evitar la creación de múltiples eventos de dosis para el mismo horario
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

# Máquina de estados del evento de dosis
    # Transiciones válidas:
    #   scheduled → alerted (llega hora de toma)
    #   alerted → taken (usuario confirma)
    #   alerted → pending (vence tiempo sin confirmar)
    #   pending → alerted (reintento permitido)
    #   pending → skipped (usuario omite o expira política)
    #   taken → synced (servidor acepta evento)
    #   skipped → synced (servidor acepta evento)
    #   pending → synced (servidor registra pendiente)

    def mark_alerted(self):
        """Transición: scheduled → alerted (llega la hora de la toma)."""
        if self.status == DoseEventStatus.SCHEDULED:
            self.status = DoseEventStatus.ALERTED

    def mark_taken(self):
        """Transición: alerted → taken (usuario confirma la toma)."""
        if self.status == DoseEventStatus.ALERTED:
            self.status = DoseEventStatus.TAKEN
            self.confirmed_at = datetime.now()

    def mark_pending(self):
        """Transición: alerted → pending (vence el tiempo sin confirmar) o pending → alerted (reintento)."""
        if self.status == DoseEventStatus.ALERTED:
            self.status = DoseEventStatus.PENDING
        elif self.status == DoseEventStatus.PENDING:
            self.status = DoseEventStatus.ALERTED

    def mark_skipped(self):
        """Transición: pending → skipped (usuario omite o expira política)."""
        if self.status == DoseEventStatus.PENDING:
            self.status = DoseEventStatus.SKIPPED
            self.confirmed_at = datetime.now()

    def mark_synced(self):
        """Transición: taken/skipped/pending → synced (servidor acepta/registra evento)."""
        if self.status in (DoseEventStatus.TAKEN, DoseEventStatus.SKIPPED, DoseEventStatus.PENDING):
            self.sync_status = SyncStatus.SYNCED

    def mark_failed(self):
        """Transición: taken/skipped → failed (falló la sincronización)."""
        if self.status in (DoseEventStatus.TAKEN, DoseEventStatus.SKIPPED):
            self.sync_status = SyncStatus.FAILED

    def set_source(self, source: Source):
        """Establece la fuente del evento de dosis."""
        self.source = source

    def is_synced(self) -> bool:
        """Verifica si el evento de dosis está sincronizado."""
        return self.sync_status == SyncStatus.SYNCED

    def is_pending(self) -> bool:
        """Verifica si el evento de dosis está pendiente."""
        return self.status == DoseEventStatus.PENDING

    def is_taken(self) -> bool:
        """Verifica si el evento de dosis está tomado."""
        return self.status == DoseEventStatus.TAKEN

    def is_skipped(self) -> bool:
        """Verifica si el evento de dosis está saltado."""
        return self.status == DoseEventStatus.SKIPPED

    def is_scheduled(self) -> bool:
        """Verifica si el evento de dosis está programado."""
        return self.status == DoseEventStatus.SCHEDULED

    def is_alerted(self) -> bool:
        """Verifica si el evento de dosis está alertado."""
        return self.status == DoseEventStatus.ALERTED
        