from typing import Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUD
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomUpdate

class CRUDRoom(CRUD[Room, RoomCreate,None]):
    def create_with_owner(self, db:Session, *, obj_in: RoomCreate) -> Room:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_topic(self, db:Session, *, topic:str) -> Optional[Room]:
        return db.query(Room).filter(Room.topic==topic).first()
    

room = CRUDRoom(Room)