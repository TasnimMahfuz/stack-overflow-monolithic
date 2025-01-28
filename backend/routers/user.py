from fastapi import APIRouter, HTTPException

from hashing import Hash
from models import User, ShowUser
from database import db


router=APIRouter(tags=['Users'])

@router.post('/users', response_model=ShowUser)
def signup(user: User):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")

    user_dict = user.dict()  
    user_dict['password'] = Hash.bcrypt(user.password)  
    result = db.users.insert_one(user_dict) 

    user_dict['id'] = str(result.inserted_id) 

    return ShowUser(**user_dict)  



"""
@router.post('/users',response_model=ShowUser)
def signup(user:User):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already exists")
    
    user['id']=str(user['_id'])
    user.password=Hash.bcrypt(user.password)
    db.users.insert_one(user.dict())

    return user

"""