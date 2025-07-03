from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class User(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    username:str
    email:str
    
    
    items: List["Item"]= Relationship(back_populates="owner")
    