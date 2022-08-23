from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    items = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "task"

    id = Column(String, primary_key=True, index=True, nullable=False)
    text = Column(String, index=True, nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)

    user = relationship("user", back_populates="task")