from datetime import datetime

from pydantic import BaseModel


class MessageCreate(BaseModel):
    text: str


class MessageRetrieve(BaseModel):
    id: int
    text: str
    created_at: datetime