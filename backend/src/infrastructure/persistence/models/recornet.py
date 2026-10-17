from __future__ import annotations

from datetime import date, datetime
from typing import Any

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import JSON

#declaracion de la clase base para la persistencia
class Base(DeclarativeBase):
    pass

# clase modelo para la persistencia de la tabla care_relationships
class CareRelationshipModel(Base):
    __tablename__ = "care_relationships"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    caregiver_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    elderly_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="active")

# clase modelo para la persistencia de la tabla care_permissions
class CarePermissionModel(Base):
    __tablename__ = "care_permissions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    care_relationship_id: Mapped[int] = mapped_column(
        ForeignKey("care_relationships.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    code: Mapped[str] = mapped_column(String(64), nullable=False)
    revoked_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


# clase modelo para la persistencia de la tabla medications
class MedicationModel(Base):
    __tablename__ = "medications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    photo_url: Mapped[str | None] = mapped_column(Text)
    form: Mapped[str] = mapped_column(String(100), default="", nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(255), default="", nullable=False)
    created_by_user_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="active")


# clase modelo para la persistencia de la tabla treatments
class TreatmentModel(Base):
    __tablename__ = "treatments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    medication_id: Mapped[int] = mapped_column(ForeignKey("medications.id"), nullable=False, index=True)
    patient_user_id: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    creator_user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    dose: Mapped[str] = mapped_column(String(100), nullable=False)
    instructions: Mapped[str] = mapped_column(Text, default="", nullable=False)
    frequency_value: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    frequency_unit: Mapped[str] = mapped_column(String(32), default="days", nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="active", nullable=False)


# clase modelo para la persistencia de la tabla reminder_schedules
class ReminderScheduleModel(Base):
    __tablename__ = "reminder_schedules"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    treatment_id: Mapped[int] = mapped_column(
        ForeignKey("treatments.id", ondelete="CASCADE"), nullable=False, index=True
    )
    scheduled_time: Mapped[str] = mapped_column(String(16), default="", nullable=False)
    frequency_value: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    frequency_unit: Mapped[str] = mapped_column(String(32), default="days", nullable=False)
    days_of_week: Mapped[list[int]] = mapped_column(JSON, default=list, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)


# # Se mantiene como una pequeña superficie de exportación para pruebas de infraestructura y futuros adaptadores.
Model = Any
