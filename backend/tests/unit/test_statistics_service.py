import pytest
from src.domain.entities.statistics_snapshots import StatisticsSnapshots
from src.domain.services.statistics_service import StatisticsService, Statistics


class ConcreteStatisticsService(StatisticsService):
    def __init__(self) -> None:
        self.storage: dict[str, StatisticsSnapshots] = {}

    def get_by_id(self, statistics_id: str) -> StatisticsSnapshots | None:
        return self.storage.get(statistics_id)

    def update(self, statistics_id: str, statistics: StatisticsSnapshots) -> StatisticsSnapshots | None:
        self.storage[statistics_id] = statistics
        return statistics

    def delete(self, statistics_id: str) -> bool:
        return self.storage.pop(statistics_id, None) is not None

    def get_pending(self) -> list[StatisticsSnapshots]:
        return list(self.storage.values())


def test_statistics_service_is_abstract() -> None:
    with pytest.raises(TypeError):
        StatisticsService()  # type: ignore[abstract]


def test_statistics_alias_points_to_statistics_snapshots() -> None:
    assert Statistics is StatisticsSnapshots


def test_concrete_statistics_service_crud_operations() -> None:
    service = ConcreteStatisticsService()
    snapshot = StatisticsSnapshots(id="stat-1", user_id="user-123", metrics={"adherence": 85.0})

    assert service.get_by_id("stat-1") is None
    assert service.update("stat-1", snapshot) == snapshot
    assert service.get_by_id("stat-1") == snapshot
    assert service.get_pending() == [snapshot]
    assert service.delete("stat-1") is True
    assert service.get_by_id("stat-1") is None
