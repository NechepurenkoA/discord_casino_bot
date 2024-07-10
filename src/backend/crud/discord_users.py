from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.models import discord_users


def get_user_by_id(db: AsyncSession, discord_id: int):
    return (
        db.query(discord_users.DiscordUser)
        .filter(discord_users.DiscordUser.discord_id == discord_id)
        .first()
    )
