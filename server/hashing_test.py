import bcrypt

password = "my_secure_password"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print(f"Hashed Password: {hashed_password}")


is_valid = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
print(f"Password is valid: {is_valid}")
