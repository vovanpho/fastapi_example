from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post('/room', response_model=schemas.Room)
def create_room(
    *,
    db:Session = Depends(deps.get_db),
    topic: str = Body(...),
    password: int = Body(...),
    is_public: bool = Body(...),
    current_user: models.User =Depends(deps.get_current_active_user)
)->Any:
    room = crud.room.get_by_topic(db=db, topic=topic)
    if room:
        raise HTTPException(status_code=400,
        detail="topic already exists")
    room_in = schemas.RoomCreate(topic=topic, password=password, is_public=is_public)
    room = crud.room.create_with_owner(db=db, obj_in=room_in)
    if room:
        user_room_in = schemas.UserRoomCreate(user_id=current_user.id, room_id=room.id)
        crud.userroom.create_relation(db=db, obj_in=user_room_in)
    else:
        raise HTTPException(status_code=400,
        detail="room not exists")
    return room