from typing import Optional
from pydantic import BaseModel

class UserRoomBase(BaseModel):
    user_id: Optional[int]=None
    room_id: Optional[int]=None

class UserRoomCreate(UserRoomBase):
    user_id: int
    room_id: int

class UserRoomInDBBase(UserRoomBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True

class UserRoom(UserRoomInDBBase):
    pass
class UserRoomInDB(UserRoomInDBBase):
    pass