from fastapi import Depends

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from chat.service.base import BaseService
from chat.models.chat import Chat
from chat.core.datastore import async_session_provider

def get_chat_service(
    session: Annotated[AsyncSession, Depends(async_session_provider)]
):
    return ChatService(session, Chat)

class ChatService(BaseService):

    pass
