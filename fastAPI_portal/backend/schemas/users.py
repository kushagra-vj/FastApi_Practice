from lib2to3.pytree import Base
from typing import Optional
from pydantic  import BaseModel, EmailStr


class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str