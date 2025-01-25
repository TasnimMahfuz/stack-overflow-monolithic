import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"


def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=30) 
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"


token = create_access_token({"user_id": 123,"type": "dictionary","difficuly":"easy"})
print(f"Token: {token}")

decoded = decode_token(token)
print(f"Decoded Data: {decoded}")
