from datetime import date, datetime, timezone

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.domain.exceptions.domain_exceptions import UnauthorizedAccess
from src.domain.entities.reminder import ReminderSchedule
from src.infrastructure.persistence.models.recornet import (
    Base,
    CarePermissionModel,
    CareRelationshipModel,
    MedicationModel,
    ReminderScheduleModel,
    TreatmentModel,
)
from src.infrastructure.persistence.repositories.sqlalchemy_medication_repository import (
    SqlAlchemyMedicationRepository,
)
from src.infrastructure.persistence.repositories.sqlalchemy_reminder_repository import (
    SqlAlchemyReminderRepository,
)
from src.infrastructure.persistence.repositories.sqlalchemy_treatment_repository import (
    SqlAlchemyTreatmentRepository,
)


@pytest.fixture()
def session():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        session.add_all(
            [
                CareRelationshipModel(id=1, caregiver_id=10, elderly_id=20, status="active"),
                CareRelationshipModel(id=2, caregiver_id=10, elderly_id=30, status="revoked"),
                CarePermissionModel(id="p1", care_relationship_id=1, code="view_treatments"),
                CarePermissionModel(id="p2", care_relationship_id=1, code="manage_treatments"),
                CarePermissionModel(
                    id="p3",
                    care_relationship_id=2,
                    code="view_treatments",
                    revoked_at=datetime.now(timezone.utc),
                ),
                MedicationModel(
                    id=100,
                    name="Medication linked",
                    form="tablet",
                    manufacturer="Acme",
                    created_by_user_id=10,
                    created_at=datetime.now(timezone.utc),
                    status="active",
                ),
                MedicationModel(
                    id=200,
                    name="Medication private",
                    form="tablet",
                    manufacturer="Acme",
                    created_by_user_id=30,
                    created_at=datetime.now(timezone.utc),
                    status="active",
                ),
                TreatmentModel(
                    id=1000,
                    medication_id=100,
                    patient_user_id=20,
                    creator_user_id=10,
                    dose="1 mg",
                    instructions="after breakfast",
                    frequency_value=1,
                    frequency_unit="days",
                    start_date=date(2026, 1, 1),
                    end_date=date(2026, 12, 31),
                    version=1,
                    status="active",
                ),
                TreatmentModel(
                    id=2000,
                    medication_id=200,
                    patient_user_id=30,
                    creator_user_id=30,
                    dose="2 mg",
                    instructions="at night",
                    frequency_value=1,
                    frequency_unit="days",
                    start_date=date(2026, 1, 1),
                    end_date=date(2026, 12, 31),
                    version=1,
                    status="active",
                ),
                ReminderScheduleModel(
                    id=3000,
                    treatment_id=1000,
                    scheduled_time="08:00",
                    frequency_value=1,
                    frequency_unit="days",
                    days_of_week=[0, 1, 2, 3, 4, 5, 6],
                    is_active=True,
                ),
                ReminderScheduleModel(
                    id=4000,
                    treatment_id=2000,
                    scheduled_time="20:00",
                    frequency_value=1,
                    frequency_unit="days",
                    days_of_week=[0, 1, 2, 3, 4, 5, 6],
                    is_active=True,
                ),
            ]
        )
        session.commit()
        yield session


def test_caregiver_only_sees_linked_patient_data(session: Session) -> None:
    treatments = SqlAlchemyTreatmentRepository(session)
    medications = SqlAlchemyMedicationRepository(session)
    reminders = SqlAlchemyReminderRepository(session)

    assert [item.id for item in treatments.get_by_patient_id("20", actor_id="10")] == ["1000"]
    assert treatments.get_by_id("1000", actor_id="10") is not None
    assert treatments.get_by_id("2000", actor_id="10") is None
    assert treatments.get_by_patient_id("30", actor_id="10") == []
    assert [item.id for item in medications.get_for_patient("20", actor_id="10")] == ["100"]
    assert medications.get_for_patient("30", actor_id="10") == []
    assert [item.id for item in reminders.get_for_patient("20", actor_id="10")] == ["3000"]
    assert reminders.get_for_patient("30", actor_id="10") == []


def test_unlinked_actor_cannot_read_or_mutate_reminder(session: Session) -> None:
    reminders = SqlAlchemyReminderRepository(session)
    assert reminders.get_by_id("4000", actor_id="10", patient_id="30") is None
    with pytest.raises(UnauthorizedAccess):
        reminders.delete("4000", actor_id="10", patient_id="30")

    with pytest.raises(UnauthorizedAccess):
        reminders.save(
            ReminderSchedule(treatment_id="2000", scheduled_time="21:00"),
            actor_id="10",
            patient_id="30",
        )


def test_revoked_permission_is_not_authorized_but_patient_can_read_own_data(session: Session) -> None:
    treatments = SqlAlchemyTreatmentRepository(session)
    assert treatments.get_by_patient_id("30", actor_id="10") == []
    assert [item.id for item in treatments.get_by_patient_id("30", actor_id="30")] == ["2000"]


def test_patient_can_read_own_reminder_without_caregiver_relationship(session: Session) -> None:
    reminders = SqlAlchemyReminderRepository(session)
    assert [item.id for item in reminders.get_for_patient("30", actor_id="30")] == ["4000"]
