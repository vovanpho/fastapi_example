from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
# import uuid
from app.db.base import Base
# from .relations import User_Room, Message_Room
if TYPE_CHECKING:
    from .user import User
    from .message import Message



class Room(Base):
    id = Column(Integer, primary_key=True, index= True)
    topic =  Column(String, index=True)
    password = Column(Integer, index=True)
    is_public = Column(Boolean(), default=False)
    user = relationship('User', secondary="user_room", back_populates='room')
    messages = relationship("Message", back_populates="room")
    

