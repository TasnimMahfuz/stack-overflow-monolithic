from typing import Optional
from bson import ObjectId
from pydantic import BaseModel


class Post(BaseModel):
    id: str
    title: str
    content: str
    user_id: str


class ShowPost(BaseModel):
    id: str
    title: str
    content: str
    user_id: str

    class Config:
        # This allows us to use the ObjectId as a string in the response
        json_encoders = {
            ObjectId: str  # Convert ObjectId to string automatically
        }


class User(BaseModel):
    email: str
    password: str


class ShowUser(BaseModel):
    email: str
    password: str


class Notification(BaseModel):
    id: str
    message: str
    post_id: str
    user_id: str
    created_at: str


class ShowNotification(BaseModel):
    id: str
    message: str
    post_id: str
    user_id: str
    created_at: str


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None