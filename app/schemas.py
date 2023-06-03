from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


# The pydantic model
# This is used to make use all the data provided
# in a request match up to what we want


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_time: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserInfo(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_time: datetime
    owner_id: int
    owner: UserInfo

    class Config:
        orm_mode = True


class PostVote(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # this can be less than 1, should replace with a method that allows for only 1 or 0
