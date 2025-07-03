from sqlmodel import Session, select
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

def create_item(db:Session, item:ItemCreate, owner_id:int):
    db_item= Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db:Session, item_id:int):
    return db.get(Item, item_id)


def get_items(db:Session, skip:int=0, limit:int=10):
    return db.exec(select(Item).offset(skip).limit(limit)).all()

def update_item(db:Session, item_id:int, item:ItemUpdate):
    db_item = db.get(Item, item_id)
    if not db_item:
        return None
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    
def delete_item(db:Session, item_id:int):
    db_item=db.get(Item,item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item

