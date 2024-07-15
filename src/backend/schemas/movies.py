import datetime as dt

from pydantic import BaseModel

from src.backend.models.movies import Genre


class MovieBase(BaseModel):
    title: str
    genre: list[Genre]
    date_published: dt.date


class MovieIn(MovieBase):
    pass


class MovieOut(MovieIn):
    id: int

    class Config:
        from_attributes = True
