from fastapi import APIRouter

from .endpoints import actors, movies

api_v1_router = APIRouter()
api_v1_router.include_router(
    actors.router,
    prefix="/actors",
    tags=[
        "Actors",
    ],
)
api_v1_router.include_router(
    movies.router,
    prefix="/movies",
    tags=[
        "Movies",
    ],
)
