from typing import Optional
from pydantic import BaseModel 
from datetime import timedelta
class MessageBase(BaseModel):
    message_text: Optional[str] = None
    message_time: timedelta = None

class MessageCreate(MessageBase):
    message_text: str

class MessageIndDBBase(MessageBase):
    id:int
    message_text: str
    owner_id: int
    room_id: int
    class Config:
        orm_mode=True
class Message(MessageIndDBBase):
    pass
class MessageInDB(MessageIndDBBase):
    pass

