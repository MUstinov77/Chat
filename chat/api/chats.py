from typing import Annotated

from fastapi import APIRouter, Depends, status, Query
from fastapi.exceptions import HTTPException

from chat.service.chat import get_chat_service, ChatService
from chat.schemas.chat import ChatRetrieve, ChatCreateUpdate
from chat.schemas.message import MessageCreate


chat_router = APIRouter(
    prefix="/chats",
    tags=["Chats"],
)

@chat_router.get(
    "/",
    response_model=list[ChatRetrieve],
)
async def get_all_chats(
        chat_service: Annotated[ChatService, Depends(get_chat_service)]
):
    chats = chat_service.retrieve_all()
    if not chats:
        raise HTTPException(status_code=404, detail="Chats not found")
    return chats


@chat_router.post(
    "/",
    response_model=ChatRetrieve,
    status_code=status.HTTP_201_CREATED,
)
async def crete_new_chat(
        data: ChatCreateUpdate,
        chat_service: Annotated[ChatService, Depends(get_chat_service)],
):
    chat_data = data.model_dump()
    chat = chat_service.create_instance(chat_data)
    return chat


@chat_router.get(
    "/{chat_id}",
    response_model=ChatRetrieve,
)
async def get_chat_by_id(
        chat_id: int,
        messages_limit: Annotated[int | None, Query(default=20, le=100)],
        chat_service: Annotated[ChatService, Depends(get_chat_service)]
):
    chat = chat_service.retrieve_one(chat_id)
    return chat


@chat_router.delete(
    "/{chat_id}",
    response_model=ChatRetrieve,
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_chat_by_id(
        chat_id: int,
        chat_service: Annotated[ChatService, Depends(get_chat_service)]
):
    chat = chat_service.delete_instance(chat_id)
    return chat