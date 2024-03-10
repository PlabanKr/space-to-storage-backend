from ..config.db import AsyncIOMotorClient
from ..models.user_models import UserSignup, UserLogin

__db_collection = "users"

async def create_user(conn, user_data: UserSignup):
    collection = conn[__db_collection]
    print(type(user_data))
    user = await collection.insert_one(user_data)
    return user

async def get_user(conn, user_email: str):
    collection = conn[__db_collection]
    user = await collection.find_one({"email": user_email})
    return user

async def update_user():
    pass