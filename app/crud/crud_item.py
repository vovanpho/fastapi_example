from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUD
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

# from . import models, schemas
# def get_items(db:Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()

# def create_item(db:Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id = user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

class CRUDItem(CRUD[Item, ItemCreate, ItemUpdate]):
    def create_with_owner(self, db:Session,  *,  obj_in: ItemCreate, owner_id: int) -> Item:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner( self, db:Session, *, owner_id: int, skip: int = 0, limit: int = 100) -> List[Item]:
        return(
            db.query(self.model)
            .filter(Item.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
item = CRUDItem(Item)