from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ItemCreate(ItemBase):
    title: str

class ItemUpdate(ItemBase):
    pass

# thuoc tich chia se trong mo hinh DB
class ItemInDBBase(ItemBase):
    id: int
    title: int
    owner_id: int

    class config:
        orm_mode: True

class Item(ItemInDBBase):
    pass

class ItemInDB(ItemInDBBase):
    pass



# class ItemBase(BaseModel):
#     Title: str
#     Description: Optional[str] = None
# class ItemCreate(ItemBase):
#     pass
# class Item(ItemBase):
#     id:int
#     owner_id:int
#     class Config:
#         orm_mode = True