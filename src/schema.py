from typing import List

from pydantic import BaseModel


class TaskBase(BaseModel):
    text: str


class Task(TaskBase):
    id: str
    user_id: str

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class UserBase(BaseModel):
    username: str
    email: str
    name: str
    hashed_password: str


class User(UserBase):
    id: str
    # tasks: List[Task] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass
