from pydantic import BaseModel
from datetime import datetime


class MessageCreate(BaseModel):
    text: str


class MessageRetrieve(BaseModel):
    id: int
    text: str
    created_at: datetime