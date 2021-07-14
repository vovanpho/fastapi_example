from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    
# khi nhan tu api
class UserCreate(UserBase):
    email: EmailStr
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

# vao db
class UserInDBBase(UserBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True

# them thuoc tinh tra ve via api
class User(UserInDBBase):
    pass
# them thuoc tinh luu tru db
class UserInDB(UserInDBBase):
    hashed_password: str

# class UserBase(BaseModel):
#     email: str
# class UserCreate(UserBase):
#     password: str
# class User(UserBase):
#     id:int
#     is_active: bool
#     items:List[Item] = []
#     class Config:
#         orm_mode = True