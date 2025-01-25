from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["stackoverflow_clone"]


db.users.insert_one({"email": "test@example.com", "password": "hashed_password"})


user = db.users.find_one({"email": "test@example.com"})
print(user)
