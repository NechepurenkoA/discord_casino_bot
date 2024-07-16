from pydantic import BaseModel

from src.backend.schemas.movies import MovieOutForActor


class MovieAssociationOut(BaseModel):
    movie: MovieOutForActor
    role: str

    class Config:
        from_attributes = True
