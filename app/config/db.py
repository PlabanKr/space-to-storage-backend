import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from .config import Config

load_dotenv()

db_client = None


async def get_db():
    db_name = Config.app_settings.get('db_name')
    return db_client[db_name]


async def connect_and_init_db():
    global db_client
    try:
        db_client = AsyncIOMotorClient(
            Config.app_settings.get('mongodb_url'),
            username=Config.app_settings.get('db_username'),
            password=Config.app_settings.get('db_password'),
            maxPoolSize=Config.app_settings.get('max_db_conn_count'),
            minPoolSize=Config.app_settings.get('min_db_conn_count'),
            uuidRepresentation="standard",
        )
    except Exception as e:
        raise


async def close_db_connect():
    global db_client
    if db_client is None:
        return
    db_client.close()
    db_client = None