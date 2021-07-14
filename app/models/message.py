from typing import TYPE_CHECKING
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

if TYPE_CHECKING:
    from .user import User
    from .room import Room
    # from .relations import Message_Room, Message_User


class Message(Base):
    id = Column(Integer, primary_key=True, index= True)
    message_text = Column(String, index=True)
    message_time =  Column(DateTime)

    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="messages")

    room_id = Column(Integer, ForeignKey('room.id'))
    room = relationship("Room", back_populates='messages')
