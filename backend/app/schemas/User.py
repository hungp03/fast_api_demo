from pydantic import BaseModel
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  

class UserLoginResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
    access_token: str

    class Config:
        from_attributes = True 

class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str

