from fastapi import FastAPI


app = FastAPI()

@app.get("/health")
async def health():
    return {"message": "Backend is up and running"}


@app.post("/signup")
async def signup(user_data: dict):
    if not user_data:
        raise HTTPException(status_code=400, detail="Invalid input")

    email = user_data.get("email")
    password = user_data.get("password")
    confirm_password = user_data.get("confirm_password")

    if not all([email, password, confirm_password ]):
        raise HTTPException(status_code=400, detail="Required fields missing: Email , Password and Confirm Password")

    if not email_validation(email):  
        raise HTTPException(status_code=400, detail="Invalid email")

    existing_user = next((user for user in existing_db if user["email"] == email), None)
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists")

    try:
        existing_user_db.append(user_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user") from e

    return {"message": "Signup is completed"}


@app.post("/login")
async def login(login_data: dict):
    if not login_data or "email" not in login_data or "password" not in login_data:
        raise HTTPException(status_code=400, detail="Invalid: Username and password are required")

    user = existing_user_db.get("email", login_data["email"])
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Email")

    if not password_verification(login_data["password"], user["password"]):
        raise HTTPException(status_code=401, detail="Invalid Password")

    return {"message": "Logged in successfully"}


@app.get("/userprofile")
async def userprofile():
    return {"message": "User Profile Updated Successfully"}

@app.get("/admin")
async def admin():
    return {"message": "Admin mode activated"}

@app.get("/user")
async def user():
    return {"message": "User mode activated"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

