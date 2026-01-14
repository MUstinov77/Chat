from fastapi import APIRouter, Depends


chat_router = APIRouter(
    prefix="/chats",
    tags=["Chats"],
)

@chat_router.get("/")
async def get_all_chats():
    chats = []
    return chats


@chat_router.post("/")
async def crete_new_chat():
    chat = None
    return chat


@chat_router.get("/{chat_id}")
async def get_chat_by_id(chat_id: int):
    chat = None
    return chat


@chat_router.delete("/{chat_id}")
async def delete_chat_by_id(chat_id: int):
    chat = None
    return chat