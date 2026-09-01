from datetime import date, datetime, timedelta, timezone

import pytest

from src.domain.entities.accessibility_preferences import AccessibilityPreferences
from src.domain.entities.auth_session import AuthSession, AuthSessionStatus
from src.domain.entities.care_permission import CarePermission, CarePermissionCode
from src.domain.entities.dose_events import DoseEvent, DoseEventStatus, SyncStatus
from src.domain.entities.notification import Notification, NotificationStatus
from src.domain.entities.notification_delivery import (
    NotificationDelivery,
    NotificationDeliveryStatus,
)
from src.domain.entities.notification_policy import NotificationPolicy
from src.domain.entities.password_reset_token import PasswordResetToken
from src.domain.entities.treatment import Treatment, TreatmentStatus
from src.domain.entities.user import User, UserStatus
from src.domain.value_objects.Frequency import Frequency
from src.domain.value_objects.interval import Interval, IntervalUnit


def test_accessibility_preferences_reject_invalid_text_scale() -> None:
    preferences = AccessibilityPreferences(user_id="user-1", text_scale=2.1)

    with pytest.raises(ValueError, match="text_scale"):
        preferences.validate()


def test_notification_policy_requires_usable_timing() -> None:
    policy = NotificationPolicy(
        owner_user_id="user-1",
        repeat_interval_minutes=30,
        pending_after_minutes=15,
    )

    with pytest.raises(ValueError, match="pending_after_minutes"):
        policy.validate()


def test_auth_session_can_be_revoked() -> None:
    session = AuthSession(
        user_id="user-1",
        refresh_token_hash="hash",
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1),
    )

    session.revoke()

    assert session.status == AuthSessionStatus.REVOKED
    assert session.revoked_at is not None
    assert not session.is_active()


def test_password_reset_token_is_single_use() -> None:
    token = PasswordResetToken(
        user_id="user-1",
        token_hash="hash",
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=30),
    )

    token.consume()

    assert not token.is_valid()
    with pytest.raises(ValueError, match="already been consumed"):
        token.consume()


def test_care_permission_can_be_revoked() -> None:
    permission = CarePermission(
        care_relationship_id="relationship-1",
        code=CarePermissionCode.MANAGE_TREATMENTS,
    )

    permission.revoke()

    assert not permission.is_active


def test_delivery_records_lifecycle() -> None:
    delivery = NotificationDelivery(notification_id="notification-1")

    delivery.mark_sent()
    delivery.mark_delivered()

    assert delivery.status == NotificationDeliveryStatus.DELIVERED
    assert delivery.attempted_at is not None
    assert delivery.delivered_at is not None


def test_notification_updates_its_documented_status_field() -> None:
    notification = Notification(recipient_user_id="user-1")

    notification.mark_as_sent()
    notification.mark_as_delivered()

    assert notification.status == NotificationStatus.DELIVERED
    assert notification.delivery_status == NotificationStatus.DELIVERED
    assert notification.sent_at is not None
    assert notification.delivered_at is not None


def test_dose_event_uses_idempotency_and_separate_sync_state() -> None:
    event = DoseEvent(treatment_id="treatment-1", schedule_id="schedule-1")

    event.transition_to(DoseEventStatus.ALERTED)
    event.transition_to(DoseEventStatus.TAKEN)
    event.mark_synced()

    assert event.idempotency_key
    assert event.status == DoseEventStatus.TAKEN
    assert event.sync_status == SyncStatus.SYNCED
    assert event.confirmed_at is not None


def test_user_role_is_derived_from_assignment_and_soft_delete_is_explicit() -> None:
    user = User(name="Ada", email="ada@example.com", password_hash="hash")

    user.soft_delete()

    assert user.status == UserStatus.DELETED
    assert not user.is_active
    assert user.deleted_at is not None
    assert not hasattr(user, "role")


def test_treatment_uses_singular_entity_and_valid_dates() -> None:
    treatment = Treatment(start_date=date(2026, 1, 1), end_date=date(2026, 1, 31))

    treatment.change_status(TreatmentStatus.CANCELLED)

    assert treatment.status == TreatmentStatus.CANCELLED
    assert treatment.version == 1
    assert treatment.end_date == date.today()


def test_frequency_requires_a_positive_interval() -> None:
    frequency = Frequency(interval=Interval(value=8, unit=IntervalUnit.HOURS))

    assert frequency.interval.value == 8
    assert frequency.interval.unit == IntervalUnit.HOURS
    with pytest.raises(ValueError, match="interval value"):
        Interval(value=0)


def test_care_relationship_is_the_single_authorization_source() -> None:
    from src.domain.entities.care_relationship import CareRelationship
    from src.domain.repositories.care_relationship_repository import CareRelationshipRepository
    from src.domain.services.care_authorization import CareAuthorizationService
    from src.domain.exceptions.domain_exceptions import UnauthorizedAccess

    relationship = CareRelationship(
        caregiver_id="caregiver-1",
        elderly_id="elderly-1",
        permissions={"view_treatment": True},
    )

    class InMemoryRelationships(CareRelationshipRepository):
        def get_between(self, caregiver_id: str, elderly_id: str):
            if (caregiver_id, elderly_id) == (relationship.caregiver_id, relationship.elderly_id):
                return relationship
            return None

    authorization = CareAuthorizationService(InMemoryRelationships())
    authorization.ensure_can_act("caregiver-1", "elderly-1", "view_treatment")
    with pytest.raises(UnauthorizedAccess):
        authorization.ensure_can_act("caregiver-2", "elderly-1", "view_treatment")


def test_treatment_and_medication_ports_require_authorized_care_context() -> None:
    import inspect
    from src.domain.repositories.medication_repository import MedicationRepository
    from src.domain.repositories.treatment_repository import TreatmentRepository

    treatment_params = inspect.signature(TreatmentRepository.get_by_patient_id).parameters
    medication_params = inspect.signature(MedicationRepository.get_for_patient).parameters
    assert "actor_id" in treatment_params
    assert "permission" in treatment_params
    assert "actor_id" in medication_params
    assert "permission" in medication_params
