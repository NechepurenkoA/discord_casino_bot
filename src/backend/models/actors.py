from sqlalchemy import Column, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.backend.core import Base


class Actor(Base):
    __tablename__ = "actors"

    first_name: Mapped[str] = mapped_column(nullable=False)
    second_name: Mapped[str] = mapped_column(nullable=False)
    third_name: Mapped[str] = mapped_column()
    birth_date = Column(Date, nullable=False)
    movies: Mapped[list["MovieActor"]] = relationship(back_populates="actors")  # type: ignore # noqa
