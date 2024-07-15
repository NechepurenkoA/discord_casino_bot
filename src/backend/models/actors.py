from enum import Enum

from sqlalchemy import Column, Date
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.core.database import Base


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Actor(Base):
    __tablename__ = "actors"

    first_name: Mapped[str] = mapped_column(nullable=False)
    second_name: Mapped[str] = mapped_column(nullable=False)
    third_name: Mapped[str] = mapped_column()
    birth_date = Column(Date, nullable=False)
    gender: Mapped[Gender] = mapped_column(
        postgresql.ENUM(Gender, name="genders", create_type=False)
    )
