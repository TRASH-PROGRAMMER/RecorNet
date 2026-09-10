from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.entities.reminder import ReminderSchedule


class ReminderRepository(ABC):
    """Puerto de persistencia de horarios de recordatorios autorizados.

    Las implementaciones concretas deben filtrar por una relación de cuidado
    activa y por el permiso solicitado antes de leer o modificar datos.
    """

    @abstractmethod
    def save(
        self,
        reminder: ReminderSchedule,
        *,
        actor_id: str,
        patient_id: str,
        permission: str = "manage_reminder",
    ) -> ReminderSchedule:
        """Guarda un horario dentro del contexto autorizado del paciente."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        reminder_id: str,
        *,
        actor_id: str,
        patient_id: str,
        permission: str = "view_reminder",
    ) -> Optional[ReminderSchedule]:
        """Obtiene un horario únicamente para un actor autorizado."""
        raise NotImplementedError

    @abstractmethod
    def get_for_patient(
        self,
        patient_id: str,
        *,
        actor_id: str,
        permission: str = "view_reminder",
    ) -> List[ReminderSchedule]:
        """Devuelve horarios filtrados por el paciente y la relación autorizada."""
        raise NotImplementedError

    @abstractmethod
    def delete(
        self,
        reminder_id: str,
        *,
        actor_id: str,
        patient_id: str,
        permission: str = "manage_reminder",
    ) -> bool:
        """Elimina un horario solo dentro de un contexto autorizado."""
        raise NotImplementedError
        