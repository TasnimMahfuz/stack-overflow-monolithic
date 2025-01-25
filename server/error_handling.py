from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 123:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "name": "John Doe"}
