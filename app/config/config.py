import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    version = "0.1.0"
    title = "Space to Storage Backend"

    app_settings = {
        'mongodb_url': os.getenv('MONGODB_URL'),
        'db_name': os.getenv('DB_NAME'),
        'db_username': os.getenv('DB_USERNAME'),
        'db_password': os.getenv('DB_PASSWORD'),
        'max_db_conn_count': int(os.getenv('MAX_DB_CONN_COUNT')),
        'min_db_conn_count': int(os.getenv('MIN_DB_CONN_COUNT')),
        'secret_key': os.getenv('SECRET_KEY'),
    }