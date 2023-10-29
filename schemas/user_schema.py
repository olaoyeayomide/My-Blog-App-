
from pydantic import BaseModel, EmailStr, Field
from typing import List
from uuid import UUID


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str = Field(..., min_length=3, max_length=20)
    bio: str = None
    email: EmailStr
    password: str

class UserRequest(BaseModel):
    id: str
    created_at: str
    first_name: str
    last_name: str
    username: str = Field(..., min_length=3, max_length=20)
    bio: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
      first_name: str
      last_name: str
      username: str = Field(..., min_length=3, max_length=20)
      bio: str = None
      email: EmailStr
      password: str = None, Field(..., min_length=8, max_length=12)

userDB: List[UserCreate] = [{}]
