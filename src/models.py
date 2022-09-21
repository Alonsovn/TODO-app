from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    email = Column(String, unique=True)
    name = Column(String)
    username = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)

    # tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "task"
    __table_args__ = {'extend_existing': True}

    id = Column(String, primary_key=True)
    text = Column(String)
    # user_id = Column(String, ForeignKey("user.id"))

    # user = relationship("User", back_populates="tasks")
