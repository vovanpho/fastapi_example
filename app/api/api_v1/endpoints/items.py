from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from app import crud, models, schemas 
from app.api import deps

router = APIRouter()

@router.get("/get", response_model=List[schemas.Item])
def read_items(
    *,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
     db:Session = Depends(deps.get_db), 
) -> Any:
    if crud.user.is_superuser(current_user):
        items = crud.item.get_multi(db, skip=skip, limit=limit)
    else:
        items = crud.item.get_multi_by_owner(db=db, owner_id=current_user.id, skip=skip, limit=limit)
    return items

@router.get("/{id}", response_model=schemas.Item)
def read_item(
    *,
    db:Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
)->Any:
    item = crud.item.get(db=db, id=id)
    print(item.owner_id)
    if not item: 
        raise HTTPException(status_code=404, detail="khong tim thay item")
    if not crud.user.is_superuser(current_user) and (item.owner_id !=current_user.id):
        raise HTTPException(status_code=400, detail="khong co quyen")
    return item

@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    db:Session = Depends(deps.get_db),
    item_in: schemas.ItemCreate,
    current_user:models.User = Depends(deps.get_current_active_user)
)->Any:
    item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
    return item

@router.put("/{id}", response_model=schemas.Item)
def update_item(
    *,
    db:Session = Depends(deps.get_db),
    id:int,
    item_in: schemas.ItemUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
)-> Any:
    item = crud.item.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="khong tim thay item")
    if not  (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="khong co quyen")
    item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return item

@router.delete("/{id}", response_model=schemas.Item)
def delete_item(
    *,
    db:Session =Depends(deps.get_db),
    id: int,
    current_user: models.User=Depends(deps.get_current_active_user)
)-> Any:
    item = crud.item.get(db=db, id=id) # tim check toi tai, quyen truoc khi xoa
    if not item:
        raise HTTPException(status_code=404, detail="khong tim thay item")
    if not crud.user.is_superuser(current_user) and (item.owner_id!=current_user.id):
        raise HTTPException(status_code=400, detail="khong du quyen")
    item = crud.item.remove(db=db, id=id)
    return item