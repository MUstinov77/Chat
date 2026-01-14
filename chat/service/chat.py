from fastapi import Depends

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from chat.service.base import BaseService
from chat.models.chat import Chat
from chat.models.message import Message
from chat.core.datastore import async_session_provider

def get_chat_service(
    session: Annotated[AsyncSession, Depends(async_session_provider)]
):
    return ChatService(session, Chat)

class ChatService(BaseService):

    async def retrieve_one(self, obj_id: int, message_limit=20, *args, **kwargs):
        query = (
            select(self.model).
            where(self.model.id == obj_id).
            join(Message, self.model.id == Message.chat_id).
            limit(message_limit)
        )
        result = await self.session.execute(query)
        return result.scalars().first()
