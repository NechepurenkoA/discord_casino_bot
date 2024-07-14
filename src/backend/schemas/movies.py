from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
