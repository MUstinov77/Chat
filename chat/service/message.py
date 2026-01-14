from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from chat.core.datastore import async_session_provider
from chat.models.message import Message
from chat.service.base import BaseService


def get_message_service(
    session: Annotated[AsyncSession, Depends(async_session_provider)]
):
    return MessageService(session, Message)


class MessageService(BaseService):
    pass