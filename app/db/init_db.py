from sqlalchemy.orm import Session

from app import crud, schemas
# from core.config import settings
from app.db import base
from app.db.session import  engine

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    base.Base.metadata.create_all(bind=engine)

    # user = crud.user.get_by_email(db, email="test@example.com")
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email="test@example.com",
    #         password="1234",
    #         is_superuser=True,
    #     )
    #     user = crud.user.create(db, obj_in=user_in)  # noqa: F841