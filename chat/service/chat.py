from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from chat.core.datastore import async_session_provider
from chat.models.chat import Chat
from chat.models.message import Message
from chat.service.base import BaseService


def get_chat_service(
    session: Annotated[AsyncSession, Depends(async_session_provider)]
):
    return ChatService(session, Chat)


class ChatService(BaseService):

    async def retrieve_one(self, obj_id: int, message_limit=20, *args, **kwargs):
        query = (
            select(self.model).
            where(self.model.id == obj_id)
        )
        result = await self.session.execute(query)
        return result.scalars().first()
