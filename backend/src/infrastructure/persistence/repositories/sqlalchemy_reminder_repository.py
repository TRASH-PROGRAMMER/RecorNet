from __future__ import annotations

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from src.domain.entities.reminder import ReminderSchedule
from src.domain.repositories.reminder_repository import ReminderRepository
from src.infrastructure.persistence.models.recornet import (
    CarePermissionModel,
    CareRelationshipModel,
    ReminderScheduleModel,
    TreatmentModel,
)
from src.infrastructure.persistence.repositories._authorized import (
    authorization_clause,
    int_id,
    map_reminder,
    require_authorized,
)


class SqlAlchemyReminderRepository(ReminderRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def _authorized_statement(self, patient_id: str, actor_id: str, permission: str):
        return (
            select(ReminderScheduleModel)
            .join(TreatmentModel, TreatmentModel.id == ReminderScheduleModel.treatment_id)
            .outerjoin(
                CareRelationshipModel,
                CareRelationshipModel.elderly_id == TreatmentModel.patient_user_id,
            )
            .outerjoin(
                CarePermissionModel,
                CarePermissionModel.care_relationship_id == CareRelationshipModel.id,
            )
            .where(
                TreatmentModel.patient_user_id == int_id(patient_id),
                authorization_clause(patient_id, actor_id, permission),
            )
        )

    def save(
        self,
        reminder: ReminderSchedule,
        *,
        actor_id: str,
        patient_id: str,
        permission: str = "manage_reminder",
    ) -> ReminderSchedule:
        require_authorized(self._session, patient_id, actor_id, _permission(permission, manage=True))
        model = (
            self._session.get(ReminderScheduleModel, int(reminder.id))
            if reminder.id is not None
            else None
        )
        if model is None:
            model = ReminderScheduleModel(
                treatment_id=int(reminder.treatment_id),
                scheduled_time=reminder.scheduled_time,
                frequency_value=reminder.frequency.interval.value,
                frequency_unit=reminder.frequency.interval.unit.value,
                days_of_week=reminder.days_of_week,
                is_active=reminder.is_active,
            )
            self._session.add(model)
        else:
            model.scheduled_time = reminder.scheduled_time
            model.frequency_value = reminder.frequency.interval.value
            model.frequency_unit = reminder.frequency.interval.unit.value
            model.days_of_week = reminder.days_of_week
            model.is_active = reminder.is_active
        self._session.flush()
        return map_reminder(model)

    def get_by_id(
        self,
        reminder_id: str,
        *,
        actor_id: str,
        patient_id: str,
        permission: str = "view_reminder",
    ) -> ReminderSchedule | None:
        model = self._session.scalar(
            self._authorized_statement(patient_id, actor_id, _permission(permission)).where(
                ReminderScheduleModel.id == int_id(reminder_id)
            )
        )
        return map_reminder(model) if model else None

    def get_for_patient(
        self,
        patient_id: str,
        *,
        actor_id: str,
        permission: str = "view_reminder",
    ) -> list[ReminderSchedule]:
        return [
            map_reminder(model)
            for model in self._session.scalars(
                self._authorized_statement(patient_id, actor_id, _permission(permission))
            ).all()
        ]

    def delete(
        self,
        reminder_id: str,
        *,
        actor_id: str,
        patient_id: str,
        permission: str = "manage_reminder",
    ) -> bool:
        require_authorized(self._session, patient_id, actor_id, _permission(permission, manage=True))
        model = self._session.scalar(
            self._authorized_statement(patient_id, actor_id, _permission(permission, manage=True)).where(
                ReminderScheduleModel.id == int_id(reminder_id)
            )
        )
        if model is None:
            return False
        self._session.delete(model)
        self._session.flush()
        return True


def _permission(permission: str, manage: bool = False) -> str:
    """Map legacy port names to the normalized DDL permission codes."""
    if permission in {"view_reminder", "view_treatment", "view_medication"}:
        return "view_treatments"
    if manage or permission in {"manage_reminder", "manage_treatment", "manage_medication"}:
        return "manage_treatments"
    return permission
