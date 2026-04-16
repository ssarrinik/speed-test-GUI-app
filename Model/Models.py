from datetime import datetime
from time import timezone

from sqlalchemy import ForeignKey, String, create_engine, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
import datetime as dt
from typing import List
from typing import Optional



class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(1000))
    achievements: Mapped[list['Achievement']] = relationship(back_populates="user")


class Achievement(Base):
    __tablename__ = 'achievements'
    id: Mapped[int] = mapped_column(primary_key=True)
    achieved_at: Mapped[datetime] = mapped_column(DateTime())
    time: Mapped[str] = mapped_column(String(10))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped['User'] = relationship(back_populates='achievements')
