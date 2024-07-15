import datetime as dt

from pydantic import BaseModel


class ActorBase(BaseModel):
    first_name: str
    second_name: str
    third_name: str
    birth_date: dt.date


class ActorIn(ActorBase):
    pass


class ActorOut(ActorBase):
    id: int

    class Config:
        from_attributes = True
