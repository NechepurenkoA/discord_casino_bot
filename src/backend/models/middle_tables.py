from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.backend.core import Base


class MovieActor(Base):
    __tablename__ = "movies_actors"
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"), primary_key=True)
    actor_id: Mapped[int] = mapped_column(ForeignKey("actors.id"), primary_key=True)
    movie: Mapped["Movie"] = relationship(back_populates="movies")  # type: ignore # noqa
    actor: Mapped["Actor"] = relationship(back_populates="actors")  # type: ignore # noqa
