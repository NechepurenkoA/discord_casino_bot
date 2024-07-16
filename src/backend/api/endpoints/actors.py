import http

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.backend.core.database import get_async_session
from src.backend.models.actors import Actor
from src.backend.models.movies import Movie
from src.backend.models.movies_actors import MovieActor
from src.backend.schemas.actors import ActorIn, ActorOut

router: APIRouter = APIRouter()


@router.post("/", status_code=http.HTTPStatus.CREATED)
async def create_actor(
    instance: ActorIn, session: AsyncSession = Depends(get_async_session)
) -> ActorOut:
    actor = Actor(**instance.dict())
    session.add(actor)
    await session.commit()
    await session.refresh(actor)
    return actor


@router.get(
    "/",
    response_model=list[ActorOut],
    response_model_exclude_none=True,
)
async def get_all_actors(
    session: AsyncSession = Depends(get_async_session),
) -> list[ActorOut]:
    query = await session.execute(
        select(Actor).options(
            selectinload(Actor.movies)
            .load_only(MovieActor.role, raiseload=True)
            .selectinload(MovieActor.movie)
            .load_only(Movie.title, Movie.genre, raiseload=True)
        )
    )
    return query.scalars().all()
