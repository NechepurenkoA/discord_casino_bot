from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from src.backend.config import settings


class PreBase:

    id: Mapped[int] = mapped_column(primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(
    settings.asyncpg_url.unicode_string(),
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(engine)


async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session
