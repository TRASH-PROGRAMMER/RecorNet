from __future__ import annotations

from datetime import date, datetime, time
from typing import Any
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    SmallInteger,
    String,
    Text,
    Time,
    UniqueConstraint,
    text,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.types import JSON

#declaracion de la clase base para la persistencia
class Base(DeclarativeBase):
    pass

# clase modelo para la persistencia de la tabla care_relationships
class CareRelationshipModel(Base):
    __tablename__ = "care_relationships"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    caregiver_id: Mapped[int] = mapped_column(Integer,ForeignKey("users.id"), nullable=False, index=True )
    elderly_id: Mapped[int] = mapped_column(Integer,ForeignKey("users.id"), nullable=False, index=True ,)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="active")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "caregiver_id <> elderly_id",
            name="caregiver_differs_from_elderly",
        ),
        Index(
            "idx_care_relationships_active_unique",
            "caregiver_id",
            "elderly_id",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
    )
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
    frequency: Mapped[str] = mapped_column(String(32), nullable=False, default="daily")
    weekdays: Mapped[list[int]] = mapped_column(
        ARRAY(SmallInteger).with_variant(JSON, "sqlite"), default=list, nullable=False
    )
    timezone: Mapped[str] = mapped_column(String(100), default="UTC", nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    times: Mapped[list[ReminderTimeModel]] = relationship(
        "ReminderTimeModel", back_populates="schedule", cascade="all, delete-orphan", lazy="selectin"
    )

    __table_args__ = (
        CheckConstraint(
            "frequency IN ('daily', 'weekly', 'interval')",
            name="check_reminder_schedule_frequency",
        ),
    )

    # Propiedades de compatibilidad con repositorios y entidades existentes
    @property
    def days_of_week(self) -> list[int]:
        return self.weekdays

    @days_of_week.setter
    def days_of_week(self, value: list[int]) -> None:
        self.weekdays = value

    @property
    def scheduled_time(self) -> str:
        if self.times:
            first_time = self.times[0].time_of_day
            return first_time.strftime("%H:%M") if hasattr(first_time, "strftime") else str(first_time)
        return ""

    @scheduled_time.setter
    def scheduled_time(self, value: str) -> None:
        if not value:
            self.times = []
            return
        parts = value.split(":")
        t = time(int(parts[0]), int(parts[1]))
        self.times = [ReminderTimeModel(time_of_day=t)]

    @property
    def frequency_value(self) -> int:
        return 1

    @frequency_value.setter
    def frequency_value(self, value: int) -> None:
        pass

    @property
    def frequency_unit(self) -> str:
        return "days"

    @frequency_unit.setter
    def frequency_unit(self, value: str) -> None:
        pass


# clase modelo para la persistencia de la tabla reminder_times
class ReminderTimeModel(Base):
    __tablename__ = "reminder_times"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    schedule_id: Mapped[int] = mapped_column(
        ForeignKey("reminder_schedules.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    time_of_day: Mapped[time] = mapped_column(Time, nullable=False)

    schedule: Mapped[ReminderScheduleModel] = relationship(
        "ReminderScheduleModel", back_populates="times"
    )

    __table_args__ = (
        UniqueConstraint("schedule_id", "time_of_day", name="uq_reminder_times_schedule_time"),
    )


# # Se mantiene como una pequeña superficie de exportación para pruebas de infraestructura y futuros adaptadores.
Model = Any
