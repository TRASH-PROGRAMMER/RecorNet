from types import SimpleNamespace

from src.domain.entities.dose_events import DoseEventStatus
from src.domain.services.adherence_service import AdherenceService


class InMemoryDoseEventRepository:
    def __init__(self, events: list[SimpleNamespace]) -> None:
        self.events = events

    def get_for_patient(self, patient_id: str) -> list[SimpleNamespace]:
        return self.events


def test_calculate_adherence_uses_taken_events_as_successes() -> None:
    repository = InMemoryDoseEventRepository(
        [
            SimpleNamespace(status=DoseEventStatus.TAKEN),
            SimpleNamespace(status=DoseEventStatus.SKIPPED),
            SimpleNamespace(status=DoseEventStatus.PENDING),
            SimpleNamespace(status=DoseEventStatus.SCHEDULED),
        ]
    )

    result = AdherenceService(repository).calculate_adherence("patient-1")

    assert result == 33.33333333333333


def test_calculate_adherence_returns_zero_without_completed_events() -> None:
    repository = InMemoryDoseEventRepository(
        [SimpleNamespace(status=DoseEventStatus.SCHEDULED)]
    )

    assert AdherenceService(repository).calculate_adherence("patient-1") == 0.0
