from datetime import datetime

from chat.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func, ForeignKey


class Message(Base):

    __tablename__ = "messages" # noqa

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(5000), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now()
    )
    chat_id: Mapped[int] = mapped_column(
        ForeignKey(
            "chats.id",
            ondelete="CASCADE",
            onupdate="CASCADE"
        )
    )

    chat = relationship(
        "Chat",
        uselist=False,
        back_populates="messages"
    )
