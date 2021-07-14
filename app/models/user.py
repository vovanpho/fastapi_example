from typing import TYPE_CHECKING
from sqlalchemy import Table, ForeignKey, Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base
# from .relations import User_Room, Message_User
if TYPE_CHECKING:
    from .item import Item
    from .message import Message
    # from .room import Room



class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    items = relationship("Item", back_populates="owner")
    messages = relationship("Message", back_populates="owner")
    room = relationship("Room", secondary="user_room", back_populates="user")
    

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index= True)
#     hashed_password= Column(String)
#     is_active = Column(Boolean, default = True)
#     items=relationship('Item',back_populates='owner')