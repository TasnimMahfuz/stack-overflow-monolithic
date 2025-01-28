from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from server_2.database import db
from email_validator import validate_email, EmailNotValidError

router = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    email: str
    password: str


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


@router.post("/signup")
async def signup(user: User):
    
    try:
        # Validate email format
        validate_email(user.email)
    except EmailNotValidError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    
    hashed_password = hash_password(user.password)
    new_user = {
        "email": user.email,
        "password": hashed_password
    }

    
    await db.users.insert_one(new_user)
    return {"message": "User created successfully"}


@router.post("/signin")
async def signin(user: User):
    existing_user = await db.users.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid email!")
    
    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid password!")
    
    return {"message": "Sign-in successful"}