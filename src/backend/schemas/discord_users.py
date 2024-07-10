from pydantic import BaseModel


class DiscordUserBase(BaseModel):
    discord_id: int


class DiscordUserCreate(DiscordUserBase):
    pass


class DiscordUser(DiscordUserBase):
    balance: int

    class Config:
        orm_mode = True
