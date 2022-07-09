from lib2to3.pytree import Base
from re import T
from typing import Optional
from pydantic  import BaseModel, EmailStr


#properties required during user creation
class UserCreate(BaseModel):
    username : str
    email : EmailStr
    password : str


class ShowUserResponse(BaseModel):
    username : str  
    email : EmailStr
    is_active : bool

    class Config(): #tells pydantic to convert even non dict obj to json
        orm_mode = True