from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
    )

from chat.models.base import Base

async_session_maker: async_sessionmaker[AsyncSession] | None = None
async_engine: AsyncEngine | None = None


async def init_db():
    global async_engine, async_session_maker

    async_engine = create_async_engine(
        "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres",
    )

    async_session_maker = async_sessionmaker(async_engine)

async def clean_db():
    global async_engine

    if async_engine:
        await async_engine.dispose()
        async_engine = None


async def get_postgres_session():
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def async_session_provider(
        session: Annotated[AsyncSession, Depends(get_postgres_session)]
):
    return session