from __future__ import annotations

from datetime import datetime
from typing import TypeVar

from sqlalchemy import and_, or_, select
from sqlalchemy.orm import Session

from src.domain.entities.care_relationship import CareRelationship, CareRelationshipStatus
from src.domain.entities.medication import Medication, MedicationStatus
from src.domain.entities.reminder import ReminderSchedule
from src.domain.entities.treatment import Treatment, TreatmentStatus
from src.domain.exceptions.domain_exceptions import UnauthorizedAccess
from src.domain.value_objects.Frequency import Frequency
from src.domain.value_objects.dosage import Dosage
from src.domain.value_objects.interval import Interval, IntervalUnit
from src.infrastructure.persistence.models.recornet import (
    CarePermissionModel,
    CareRelationshipModel,
    MedicationModel,
    ReminderScheduleModel,
    TreatmentModel,
)

T = TypeVar("T")


def normalize_permission(permission: str) -> str:
    if permission in {"view_medication", "view_treatment", "view_reminder"}:
        return "view_treatments"
    if permission in {"manage_medication", "manage_treatment", "manage_reminder"}:
        return "manage_treatments"
    return permission


def int_id(value: str | int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"numeric repository id required, got {value!r}") from exc


def authorization_clause(patient_id: str | int, actor_id: str | int, permission: str):
    """Predicate used together with the explicit relationship/permission joins."""
    permission = normalize_permission(permission)
    patient = int_id(patient_id)
    actor = int_id(actor_id)
    return or_(
        actor == patient,
        and_(
            CareRelationshipModel.caregiver_id == actor,
            CareRelationshipModel.elderly_id == patient,
            CareRelationshipModel.status == "active",
            CarePermissionModel.code == permission,
            CarePermissionModel.revoked_at.is_(None),
        ),
    )


def require_authorized(session: Session, patient_id: str | int, actor_id: str | int, permission: str) -> None:
    permission = normalize_permission(permission)
    stmt = (
        select(CareRelationshipModel.id)
        .join(
            CarePermissionModel,
            CarePermissionModel.care_relationship_id == CareRelationshipModel.id,
        )
        .where(
            CareRelationshipModel.caregiver_id == int_id(actor_id),
            CareRelationshipModel.elderly_id == int_id(patient_id),
            CareRelationshipModel.status == "active",
            CarePermissionModel.code == permission,
            CarePermissionModel.revoked_at.is_(None),
        )
    )
    if int_id(actor_id) != int_id(patient_id) and session.scalar(stmt) is None:
        raise UnauthorizedAccess(
            f"actor {actor_id} is not authorized for {permission} on patient {patient_id}"
        )


def map_medication(model: MedicationModel) -> Medication:
    return Medication(
        id=str(model.id),
        name=model.name,
        description=model.description,
        photo_url=model.photo_url,
        form=model.form,
        manufacturer=model.manufacturer,
        created_by_user_id=str(model.created_by_user_id),
        created_at=model.created_at,
        status=MedicationStatus(model.status),
    )


def map_treatment(model: TreatmentModel) -> Treatment:
    amount, _, unit = (model.dose or "0").partition(" ")
    return Treatment(
        id=str(model.id),
        medication_id=model.medication_id,
        patient_user_id=model.patient_user_id,
        created_by_user_id=model.creator_user_id,
        dosage=Dosage(float(amount), unit),
        instructions=model.instructions,
        frequency=Frequency(Interval(model.frequency_value, IntervalUnit(model.frequency_unit))),
        start_date=model.start_date,
        end_date=model.end_date,
        version=model.version,
        status=TreatmentStatus(model.status),
    )


def map_reminder(model: ReminderScheduleModel) -> ReminderSchedule:
    return ReminderSchedule(
        id=str(model.id),
        treatment_id=str(model.treatment_id),
        scheduled_time=model.scheduled_time,
        frequency=Frequency(Interval(model.frequency_value, IntervalUnit(model.frequency_unit))),
        days_of_week=list(model.days_of_week or []),
        is_active=model.is_active,
    )


def relationship_from_models(relationship: CareRelationshipModel, permissions: list[str]) -> CareRelationship:
    return CareRelationship(
        id=str(relationship.id),
        caregiver_id=str(relationship.caregiver_id),
        elderly_id=str(relationship.elderly_id),
        permissions={permission: True for permission in permissions},
        status=CareRelationshipStatus.ACTIVE if relationship.status == "active" else CareRelationshipStatus.INACTIVE,
    )
