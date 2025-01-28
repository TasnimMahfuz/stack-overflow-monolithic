import motor.motor_asyncio
from fastapi import FastAPI


app = FastAPI()

MONGO_URL = "mongodb://localhost:27017"

DB_NAME = "stack_overflow_2"


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
