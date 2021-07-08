from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()

@router.get("/", response_model=List[schemas.User])
def read_users(
    db:Session =Depends(deps.get_db), 
    skip:int = 0, 
    limit:int = 100, 
    current_user: models.User = Depends(deps.get_current_active_superuser)
    ) -> Any:
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users

# @router.post("/", response_model=schemas.User)
# def create_user(
#         *,
#         db: Session = Depends(deps.get_db),
#         user_in: schemas.UserCreate,
#         current_user: models.User = Depends(deps.get_current_active_superuser)
#     ) -> Any:
#     user = crud.user.get_by_email(db, email = user_in.email)
#     if user:
#         raise HTTPException(
#             status_code = 400,
#             detail="The user with usesrname already exists in the system.")
#     user = crud.user.create(db, obj_in = user_in)
#     if settings.EMAIL_ENABLED and user_in.email:
#         send_new_account_email(
#             email_to=user_in.email,
#             username = user_in.email,
#             password = user_in.password
#         )
#     return user

@router.post("/register", response_model=schemas.User)
def create_user_open(
    *,
    db:Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server")
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code = 400,
            detail="the user with username already exists in the system")
    user_in = schemas.UserCreate(password=password, email=email, full_name= full_name)
    user = crud.user.create(db, obj_in = user_in)
    return user
