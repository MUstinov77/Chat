from fastapi import Depends
from typing import Annotated
from chat.models.message import Message
from sqlalchemy.ext.asyncio import AsyncSession
from chat.service.base import BaseService

from chat.core.datastore import async_session_provider


def get_message_service(
    session: Annotated[AsyncSession, Depends(async_session_provider)]
):
    return MessageService(session, Message)


class MessageService(BaseService):
    pass