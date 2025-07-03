from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from models.item import User
from schemas import item




app = FastAPI(title="lets we build fastapi appliction", description="this high performance webframework")

@app.get("/user")
async def read_user():
    return {"message": "this user access"}

@app.post("/users")
async def usercreate(usercreate:User):
    return usercreate
