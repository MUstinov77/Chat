from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from fastapi.exceptions import HTTPException

from chat.schemas.chat import ChatCreateUpdate, ChatRetrieve
from chat.schemas.message import MessageCreate, MessageRetrieve
from chat.service.chat import ChatService, get_chat_service
from chat.service.message import MessageService

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
    chats = await chat_service.retrieve_all()
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
    chat = await chat_service.create_instance(chat_data)
    return chat


@chat_router.get(
    "/{chat_id}",
    response_model=ChatRetrieve,
)
async def get_chat_by_id(
        chat_id: int,
        chat_service: Annotated[ChatService, Depends(get_chat_service)],
        messages_limit: Annotated[int | None, Query(le=100)] = 20,
):
    chat = await chat_service.retrieve_one(chat_id, messages_limit)
    return chat


@chat_router.delete(
    "/{chat_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_chat_by_id(
        chat_id: int,
        chat_service: Annotated[ChatService, Depends(get_chat_service)]
):
    await chat_service.delete_instance(chat_id)
    return


@chat_router.post(
    "/{chat_id}/messages",
    response_model=MessageRetrieve,
    status_code=status.HTTP_201_CREATED
)
async def send_message(
        chat_id: int,
        data: MessageCreate,
        chat_service: Annotated[MessageService, Depends(get_chat_service)]
):
    message_data = data.model_dump()
    message_data["chat_id"] = chat_id
    message = await chat_service.create_instance(message_data)
    if not message:
        ...
    return message
