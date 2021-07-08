from datetime import datetime, timedelta
from typing import Optional, Union, Any
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from .config import settings



pwd_context =CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30




# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user =fake_decode_token(token)
#     if not user: 
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#             headers={"WWW-Authenticate": "Bearer"}    
#         )
#     return user

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> bool:
    return pwd_context.hash(password)


def authenticate_user(user, username: str, password: str):
    if not username == user["email"]:
        return False
    hashed_password = get_password_hash(user["password"])
    if not verify_password(password, hashed_password):
        return False
    return user

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    # to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES) #settings.ACCESS_TOKEN_EXPIRE_MINUTES
    to_encode={"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
