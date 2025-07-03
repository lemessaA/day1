from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate
from app.crud import item as crud_item



router = APIRouter(prefix="/items", tags=["items"])
@router.post("/", response_model=ItemRead)
def create_item(
    item:ItemCreate,
    db:Session=Depends(get_session)
):
    return crud_item.create_item(db, item, owner_id=1)

@router.get("/", response_model=list[ItemRead])
def read_items(skip:int=0, limit:int=10, db:Session=Depends(get_session)):
    return crud_item.get_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ItemRead)
def read_item(item_id:int, db:Session=Depends(get_session)):
    item = crud_item.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@router.put("/{item_id}", response_model=ItemRead)
def update_item(item_id:int, item:ItemUpdate, db:Session=Depends(get_session)):
    updated = crud_item.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="item not found ")
    return updated
@router.delete("/{item_id}")
def delete_item(item_id:int, db:Session=Depends(get_session)):
    deleted=crud_item.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="item not found")
    return {"ok":True}
    