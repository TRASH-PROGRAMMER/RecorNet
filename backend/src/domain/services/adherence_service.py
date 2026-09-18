from src.domain.entities.dose_events import DoseEventStatus
from src.domain.repositories.dose_event_repository import DoseEventRepository


class AdherenceService:
    """Calcula la adherencia a partir del historial de eventos de dosis."""

    def __init__(self, dose_event_repository: DoseEventRepository) -> None:
        self._dose_event_repository = dose_event_repository

    def calculate_adherence(self, user_id: str) -> float:
        """Devuelve el porcentaje de dosis tomadas en eventos finalizados.

        Los eventos futuros o todavía en alerta no se incluyen en el
        denominador. Las dosis tomadas cuentan como adherencia y las dosis
        pendientes u omitidas como incumplidas.
        """
        dose_events = self._dose_event_repository.get_for_patient(user_id)
        completed_events = [
            event
            for event in dose_events
            if event.status
            in {
                DoseEventStatus.TAKEN,
                DoseEventStatus.PENDING,
                DoseEventStatus.SKIPPED,
            }
        ]

        if not completed_events:
            return 0.0

        taken_doses = sum(
            event.status == DoseEventStatus.TAKEN for event in completed_events
        )
        return (taken_doses / len(completed_events)) * 100.0
