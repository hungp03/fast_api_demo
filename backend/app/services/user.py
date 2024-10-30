from fastapi import  status, HTTPException
from sqlalchemy.orm import Session
from models import User
from core.auth import hash_password, create_access_token, verify_password, verify_token
from schemas import UserLogin, UserRegister, UserLoginResponse, UserResponse

def login_user(login_request: UserLogin, db: Session):
    user = db.query(User).filter(User.username == login_request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not verify_password(login_request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"id":user.id, "username": user.username})
    
    user_info = UserLoginResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        is_active=user.is_active,
        created_at=user.created_at,
        access_token=access_token
    )
    
    return user_info

def register_user(user: UserRegister, db: Session):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserResponse(
        id=new_user.id,
        username=new_user.username,
        email=new_user.email,
        is_active=new_user.is_active,
        created_at=new_user.created_at
    )

def get_current_user_token(token: str, db:Session):
    payload = verify_token(token)
    username = payload.get("name")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        is_active=user.is_active,
        created_at=user.created_at
    )