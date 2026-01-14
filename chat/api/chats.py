from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from chat.service.chat import get_chat_service, ChatService


chat_router = APIRouter(
    prefix="/chats",
    tags=["Chats"],
)

@chat_router.get("/")
async def get_all_chats(
        chat_service: Annotated[ChatService, Depends(get_chat_service)]
):
    chats = chat_service.retrieve_all()
    if not chats:
        raise HTTPException(status_code=404, detail="Chats not found")
    return chats


@chat_router.post("/")
async def crete_new_chat(
        chat_service: Annotated[ChatService, Depends(get_chat_service)],
):
    chat = chat_service.create_instance(...)
    return chat


@chat_router.get("/{chat_id}")
async def get_chat_by_id(
        chat_id: int,
        chat_service: Annotated[ChatService, Depends(get_chat_service)]
):
    chat = chat_service.retrieve_one(chat_id)
    return chat


@chat_router.delete("/{chat_id}")
async def delete_chat_by_id(
        chat_id: int,
        chat_service: Annotated[ChatService, Depends(get_chat_service)]
):
    chat = chat_service.delete_instance(chat_id)
    return chat