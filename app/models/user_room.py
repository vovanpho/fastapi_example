from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from typing import TYPE_CHECKING

from app.db.base import Base
# if TYPE_CHECKING:
from .message import Message
from .room import Room
from .user import User


class User_Room(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship("User", backref = backref("user_room", uselist=False))  
    room_id= Column(Integer, ForeignKey('room.id'))
    # room = relationship("Room", backref=backref("user_room", uselist=False))

