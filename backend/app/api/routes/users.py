from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session
from api.deps import get_db
from core.auth import oauth2_scheme
from schemas import UserLogin, UserRegister, BaseResponse
from services.user import login_user, register_user, get_current_user_token

router = APIRouter()

@router.post("/register", response_model=BaseResponse)
async def register(user: UserRegister, db: Session = Depends(get_db)):
    new_user = register_user(user, db)
    return BaseResponse(
        status_code = status.HTTP_201_CREATED,
        message = "Register successful",
        data = new_user
    )

# Đăng nhập
@router.post("/login", response_model=BaseResponse)
async def login(login_request: UserLogin, db: Session = Depends(get_db)):
    user_info = login_user(login_request, db)
    
    return BaseResponse(
        status_code=status.HTTP_200_OK,
        data=user_info,
        message="Login successful"
    )


# API endpoint with token
@router.get("/me", response_model=BaseResponse)
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_current_user_token(token, db)
    return BaseResponse(
        status_code=status.HTTP_200_OK,
        data=user,
        message="Get current user"
    )
