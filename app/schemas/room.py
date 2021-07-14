from typing import Optional
from pydantic import BaseModel

class RoomBase(BaseModel):
    topic: Optional[str] = None
    is_public: Optional[bool] = False

class RoomCreate(RoomBase):
    topic: str
    password: int
    is_public: bool = False
    
class RoomUpdate(RoomBase):
    topic: str
    password: int

class RoomInDBBase(RoomBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class Room(RoomInDBBase):
    pass

class RoomInDB(RoomInDBBase):
    pass 