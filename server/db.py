from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI


MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "stack_overflow_test"


app = FastAPI()


client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
