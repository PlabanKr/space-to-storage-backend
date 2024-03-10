from fastapi import APIRouter, HTTPException, Depends

from ..config.db import get_db
from ..models.user_models import UserLogin, UserSignup, User
from ..schemas.user import get_user, create_user
from ..utils.auth import verify_password, get_password_hash

router = APIRouter()

@router.post("/signup")
async def signup(user_data: UserSignup, db=Depends(get_db)):
    user_data = user_data.dict()
    # print(user_data)
    if not user_data:
        raise HTTPException(status_code=400, detail="Invalid input")

    first_name = user_data["first_name"]
    last_name = user_data["last_name"]
    email = user_data["email"]
    password = user_data["password"]
    confirm_password = user_data["confirm_password"]

    if not all([first_name, last_name, email, password, confirm_password]):
        raise HTTPException(status_code=400, detail="Required fields missing: Email , Password and Confirm Password")

    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Password and Confirm Password do not match")

    # if not email_validation(email):  
    #     raise HTTPException(status_code=400, detail="Invalid email")

    existing_user = await get_user(db, email)
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists")

    try:
        hashed_password = get_password_hash(password)
        new_user_data = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password, is_admin=False) 
        new_user = await create_user(db, new_user_data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user") from e

    return {"message": f"{new_user.inserted_id} created successfully"}


# @router.post("/login")
# async def login(login_data: UserLogin):
#     if not login_data or "email" not in login_data or "password" not in login_data:
#         raise HTTPException(status_code=400, detail="Invalid: Username and password are required")

#     user = existing_user_db.get("email", login_data["email"])
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid Email")

#     if not password_verification(login_data["password"], user["password"]):
#         raise HTTPException(status_code=401, detail="Invalid Password")

#     return {"message": "Logged in successfully"}


# @router.get("/profile")
# async def userprofile():
#     return {"message": "User Profile Updated Successfully"}

# @router.get("/admin")
# async def admin():
#     return {"message": "Admin mode activated"}

# @router.get("/user")
# async def user():
#     return {"message": "User mode activated"}

# @router.exception_handler(HTTPException)
# async def http_exception_handler(request, exc):
#     return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

