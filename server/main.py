from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "detail": f"Details for item {item_id}"}

@app.get("/test/{test_id}")
def trying_something(test_id: int):
    return {"test_id":test_id, "details": f"Details for test: {test_id}"}
