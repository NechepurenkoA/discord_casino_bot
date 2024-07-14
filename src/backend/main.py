from fastapi import FastAPI

from backend.routers import movies

app = FastAPI()
app.include_router(movies.router)
