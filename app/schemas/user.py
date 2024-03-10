from ..config.db import AsyncIOMotorClient
from ..models.user_models import UserSignup, UserLogin, UserUpdate

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

async def update_user(conn, user_data: dict, user_email: str):
    print(user_data)
    collection = conn[__db_collection]
    old_user = await collection.find_one({"email": user_email})
    user_document_id = old_user["_id"]
    result = await collection.update_one({"_id": user_document_id}, {"$set": user_data})
    updated_user = await collection.find_one({"_id": user_document_id})
    return {"Updated user": updated_user, "Modified Count": result.modified_count}
    