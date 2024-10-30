from fastapi import APIRouter

import api.routes.users as users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])