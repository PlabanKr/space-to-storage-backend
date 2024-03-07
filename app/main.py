from fastapi import FastAPI

from .config.db import connect_and_init_db
from .routers import user_routes

app = FastAPI()

# DB Event Handlers
@app.on_event("startup")
async def startup_event():
    print("Connecting to database")
    await connect_and_init_db()

@app.get("/health")
async def health():
    return {"message": "Backend is up and running"}

# APIs
app.include_router(user_routes.router, prefix="/user", tags=["user"])