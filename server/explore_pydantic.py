from pydantic import BaseModel, EmailStr
from fastapi import FastAPI

app = FastAPI()


class User(BaseModel):
    email: EmailStr
    password: str

@app.post("/signup/")
def create_user(user: User):
  
    return {"message": f"User {user.email} registered successfully!"}
