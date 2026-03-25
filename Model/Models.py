from sqlalchemy import ForeignKey, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List
from typing import Optional



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(1000))




