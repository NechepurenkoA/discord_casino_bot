from enum import Enum

from sqlalchemy import Column, Date
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base


class Genre(Enum):
    HORROR = "Horror"
    ROMANCE = "Romance"
    ACTION = "Action"
    THRILLER = "Thriller"
    DOCUMENTARY = "Documentary"


class Movie(Base):
    __tablename__ = "movies"

    title: Mapped[str] = mapped_column(nullable=False)
    genre: Mapped[Genre] = mapped_column(postgresql.ENUM(Genre))
    date_published = Column(Date, nullable=False)
    actors: Mapped[list["MovieActor"]] = relationship(back_populates="movies")  # noqa
