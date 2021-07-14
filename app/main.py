# import module
import uvicorn
from typing import Optional ,List
from fastapi import FastAPI ,Query, Path, Body, Header, Depends, HTTPException, status
from sqlalchemy.orm import Session
from functools import lru_cache
# from api import models, schemas, crud
from app.db.session import engine, database
from app.db import base
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.api_v1.api import api_router

@lru_cache()
def get_settings():
    return settings

app = FastAPI(
    #Metadata
    title = settings.PROJECT_NAME, 
    description="mo ta ve project", 
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    #Behind a proxy (dai dien)
    # servers=[
    #     {
    #         "url": "/api/v1"
    #     }
    # ]
)
# middleware & CORS
origins = [
    "http://127.0.0.1:8000",
    "http://localhost",
]
# if settings.BACKEND_CORS_ORIGINS:
app.add_middleware(
        CORSMiddleware,
        allow_origins= origins,# [(origin) for origins in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)  
app.include_router(api_router, prefix = settings.API_V1_STR)

# @app.on_event("startup")
# async def startup():
#     await database.connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)

#
# models.Base.metadata.create_all(bind=engine)
#Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user: 
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)

# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int=0, limit: int=100, db:Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users

# @app.get("/user/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session=Depends(get_db)):
#     db_user=crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @app.post("/user/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(user_id: int, item:schemas.ItemCreate, db: Session = Depends(get_db)):
#     return crud.create_item(db, item=item, user_id=user_id)

# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
