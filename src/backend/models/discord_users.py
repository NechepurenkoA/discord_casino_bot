from sqlalchemy.orm import Mapped, mapped_column
from src.backend.database import Base


class DiscordUser(Base):
    __tablename__ = "discord_users"

    discord_id: Mapped[int] = mapped_column("discord_id", unique=True, nullable=False)
    balance: Mapped[int] = mapped_column("balance", default=0, nullable=False)
