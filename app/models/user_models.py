from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserSignup(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    confirm_password: str

class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_admin: bool
    