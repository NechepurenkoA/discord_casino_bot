from fastapi import FastAPI
from src.backend.routers import discord_users

app = FastAPI()
app.include_router(discord_users.router)
