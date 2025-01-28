from fastapi import FastAPI
from server_2.routes import auth

app = FastAPI()
app.include_router(auth.router)

@app.get("/")
async def health_check():
    return {"message": "Server is running!"}
