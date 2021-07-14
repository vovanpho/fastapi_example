from typing import Optional, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUD
from app.models.user_room import User_Room
from app.schemas.user_room import UserRoomCreate 

class CRUDUserRoom(CRUD[User_Room, UserRoomCreate, None]):
    def create_relation(self, db: Session, *, obj_in: UserRoomCreate)->User_Room:
        db_obj= User_Room(
            user_id = obj_in.user_id,
            room_id = obj_in.room_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    

userroom = CRUDUserRoom(User_Room)