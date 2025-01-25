from fastapi import FastAPI, HTTPException
from db import db
from models import User
from bson import ObjectId

app = FastAPI()


@app.post("/signup")
async def create_user(user: User):
    users_collection = db.users  
    
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    
    result = await users_collection.insert_one(user.dict())
    if result.inserted_id:
        return {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create user")




@app.get("/users")
async def get_users():
    users_collection = db.users
    users = await users_collection.find().to_list(100)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    
   
    for user in users:
        user["_id"] = str(user["_id"])
    
    return {"users": users}
