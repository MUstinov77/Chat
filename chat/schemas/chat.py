from pydantic import BaseModel
from datetime import datetime

from chat.schemas.message import MessageRetrieve


class ChatCreateUpdate(BaseModel):
    title: str


class ChatRetrieve(BaseModel):
    id: int
    title: str
    created_at: datetime

    messages: list[MessageRetrieve]