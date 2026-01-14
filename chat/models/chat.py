from datetime import datetime

from chat.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func


class Chat(Base):

    __tablename__ = "chats" # noqa

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=func.now()
    )

    messages = relationship(
        "Message",
        uselist=True,
        back_populates="chat",
        cascade="all, delete"
    )
