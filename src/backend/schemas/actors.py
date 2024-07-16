import datetime as dt
from typing import Optional

from pydantic import BaseModel

from src.backend.models.actors import Gender
from src.backend.schemas.movies_actors import MovieAssociationOut


class ActorBase(BaseModel):
    first_name: str
    second_name: str
    third_name: Optional[str] = ""
    birth_date: dt.date
    gender: Gender


class ActorIn(ActorBase):
    pass


class ActorOut(ActorBase):
    id: int
    movies: list[MovieAssociationOut]

    class Config:
        from_attributes = True
