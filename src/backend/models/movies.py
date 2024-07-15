from enum import Enum

from sqlalchemy import Column, Date
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column

from src.backend.core.database import Base


class Genre(Enum):
    HORROR: str = "Horror"
    ROMANCE: str = "Romance"
    ACTION: str = "Action"
    THRILLER: str = "Thriller"
    DOCUMENTARY: str = "Documentary"
    DRAMA: str = "Drama"
    BIOGRAPHY: str = "Biography"
    HISTORY: str = "History"


class Movie(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    genre: Mapped[list[Genre]] = mapped_column(
        postgresql.ARRAY(postgresql.ENUM(Genre, name="genres", create_type=False))
    )
    date_published = Column(Date, nullable=False)
