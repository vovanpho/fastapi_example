from typing import Optional
from pydantic import BaseModel

# class ItemBase(BaseModel):
#     title: str = None
#     description: Optional[str] = None

# class ItemCreate(ItemBase):
#     title: str

# class ItemUpdate(ItemBase):
#     pass # co nghia la ca cac truong ItemBase

# # thuoc tich chia se trong mo hinh DB
# class ItemInDBBase(ItemBase):
#     id: int
#     title: str
#     owner_id: int

#     class config:
#         orm_mode: True

# # return client
# class Item(ItemInDBBase):
#     pass

# # return DB
# class ItemInDB(ItemInDBBase):
#     pass



class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
class ItemCreate(ItemBase):
    title: str
    pass
class ItemUpdate(ItemBase):
    pass # co nghia la ca cac truong ItemBase
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int
    class Config:
        orm_mode = True
class Item(ItemInDBBase):
    pass
class ItemInDB(Item):
    pass