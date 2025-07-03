from sqlmodel import SQLModel, Field, Relationship
from.user import User
from typing import Optional


class Item(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    tittle:str
    description:str
    owner_id:Optional[int] = Field(default=None, foreign_key=True)
    owner:Optional[User] = Relationship(back_populates="items")
    