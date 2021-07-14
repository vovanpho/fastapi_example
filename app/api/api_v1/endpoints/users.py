from typing import Any, List
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


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

@router.get("/profile/{id}", response_model=schemas.User)
def read_user(
    *,
    db:Session = Depends(deps.get_db),
    id: int,
    current_user_active: models.User = Depends(deps.get_current_active_user),
)->Any:
    user = crud.user.get(db, id)
    if user == current_user_active:
        return user
    if not crud.user.is_superuser(current_user_active):
        raise HTTPException(
            status_code = 400,
            detail="ban chua du quyen")
    return user

@router.post("/", response_model=schemas.User)
def update_user(
    *,
    db:Session=Depends(deps.get_db),
    password: str = Body(None),
    email:EmailStr = Body(None),
    full_name:str = Body(None),
    current_user_active:models.User=Depends(deps.get_current_active_user)
)-> Any:
    current_user_data = jsonable_encoder(current_user_active)
    # print(current_user_active)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user =  crud.user.update(db=db, db_obj=current_user_active, obj_in= user_in)
    return user


#superuser

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