"""Importing models for Alembic."""

from .database import Base  # noqa
from src.backend.models import Actor, Movie, MovieActor  # noqa
from .config import settings  # noqa
