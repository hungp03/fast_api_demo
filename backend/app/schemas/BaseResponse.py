from pydantic import BaseModel
from typing import Any

class BaseResponse(BaseModel):
    status_code: int
    message: str
    data: Any