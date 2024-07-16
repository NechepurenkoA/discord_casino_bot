from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.backend.core.database import Base


class MovieActor(Base):
    __tablename__ = "movies_actors"

    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"), primary_key=True)
    actor_id: Mapped[int] = mapped_column(ForeignKey("actors.id"), primary_key=True)
    role: Mapped[str]
    actor: Mapped[list["Actor"]] = relationship(  # noqa
        "Actor", back_populates="movies"
    )
    movie: Mapped[list["Movie"]] = relationship(  # noqa
        "Movie", back_populates="actors"
    )
