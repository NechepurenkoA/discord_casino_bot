import http

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.core.database import get_async_session
from src.backend.models.movies import Movie
from src.backend.schemas.movies import MovieIn, MovieOut

router: APIRouter = APIRouter()


@router.post("/", status_code=http.HTTPStatus.CREATED)
async def create_movie(
    instance: MovieIn, session: AsyncSession = Depends(get_async_session)
) -> MovieOut:
    movie = Movie(**instance.dict())
    session.add(movie)
    await session.commit()
    await session.refresh(movie)
    return movie


@router.get(
    "/",
    response_model=list[MovieOut],
    response_model_exclude_none=True,
)
async def get_all_movies(
    session: AsyncSession = Depends(get_async_session),
) -> list[MovieOut]:
    query = await session.execute(select(Movie))
    return query.scalars().all()
