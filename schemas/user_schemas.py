
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(UserCreate):
    id: int

class UserResponse(UserUpdate):
    pass