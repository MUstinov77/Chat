from contextlib import asynccontextmanager

from fastapi import FastAPI

from chat.api.chats import chat_router
from chat.core.datastore import clean_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()

    try:
        yield
    finally:
        await clean_db()


def create_app():
    app = FastAPI(
        title="Chat",
        lifespan=lifespan
    )

    app.include_router(chat_router)

    return app