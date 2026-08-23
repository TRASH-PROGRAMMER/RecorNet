from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from enum import Enum 
import uuid
from src.domain.value_objects.idempotency_key import IdempotencyKey
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

# Métodos para cambiar el estado del evento de dosis
    def mark_taken(self):
        """Marca el evento de dosis como tomado."""  
        if self.status == DoseEventStatus.PENDING or self.status == DoseEventStatus.SCHEDULED: # si el evento de dosis está pendiente o programado
            self.status = DoseEventStatus.TAKEN # se marca como tomado
            self.confirmed_at = datetime.now() # se actualiza la fecha de confirmación
# metodo para saltar el evento de dosis 
    def mark_skipped(self):
        """Marca el evento de dosis como saltado."""  
        if self.status == DoseEventStatus.PENDING or self.status == DoseEventStatus.SCHEDULED: # si el evento de dosis está pendiente o programado
            self.status = DoseEventStatus.SKIPPED # se marca como saltado
            self.confirmed_at = datetime.now() # se actualiza la fecha de confirmación

    # Método para actualizar el estado de sincronización
    def mark_synced(self):
        """Marca el evento de dosis como sincronizado."""   
        if self.status == DoseEventStatus.TAKEN or self.status == DoseEventStatus.SKIPPED: # si el evento de dosis está tomado o saltado
            self.sync_status = SyncStatus.SYNCED # se marca como sincronizado
    
    def mark_failed(self):
        """Marca el evento de dosis como fallido."""
        if self.status == DoseEventStatus.TAKEN or self.status == DoseEventStatus.SKIPPED: # si el evento de dosis está tomado o saltado
            self.sync_status = SyncStatus.FAILED # se marca como fallido
    
    def mark_pending(self):
        """Marca el evento de dosis como pendiente."""
        if self.status == DoseEventStatus.TAKEN or self.status == DoseEventStatus.SKIPPED: # si el evento de dosis está tomado o saltado
            self.sync_status = SyncStatus.PENDING # se marca como pendiente

    # Método para actualizar la fuente del evento de dosis
    def set_source(self, source: Source):
        """Establece la fuente del evento de dosis."""
        self.source = source # se establece la fuente

    # Método para verificar si el evento de dosis está sincronizado
    def is_synced(self) -> bool:
        """Verifica si el evento de dosis está sincronizado."""
        return self.sync_status == SyncStatus.SYNCED # verifica si el estado de sincronización es sincronizado

    def is_pending(self) -> bool:
        """Verifica si el evento de dosis está pendiente."""
        return self.status == DoseEventStatus.PENDING # verifica si el estado es pendiente

    def is_taken(self) -> bool:
        """Verifica si el evento de dosis está tomado."""
        return self.status == DoseEventStatus.TAKEN # verifica si el estado es tomado

    def is_skipped(self) -> bool:
        """Verifica si el evento de dosis está saltado."""
        return self.status == DoseEventStatus.SKIPPED # verifica si el estado es saltado

    def is_scheduled(self) -> bool:
        """Verifica si el evento de dosis está programado."""
        return self.status == DoseEventStatus.SCHEDULED # verifica si el estado es programado
        