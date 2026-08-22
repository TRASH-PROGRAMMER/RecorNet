from datetime import datetime, timedelta, timezone

import pytest

from src.domain.entities.accessibility_preferences import AccessibilityPreferences
from src.domain.entities.auth_session import AuthSession, AuthSessionStatus
from src.domain.entities.care_permission import CarePermission, CarePermissionCode
from src.domain.entities.notification_delivery import (
    NotificationDelivery,
    NotificationDeliveryStatus,
)
from src.domain.entities.notification_policy import NotificationPolicy
from src.domain.entities.password_reset_token import PasswordResetToken


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
