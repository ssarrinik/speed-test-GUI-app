import os
import pandas as pd
import random
from Model.Models import User, Base, Achievement
from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
import bcrypt
import datetime as dt

class ModelService:
    def __init__(self):
        self.engine = create_engine(os.environ.get("DATABASE_URI"), echo=False)
        Base.metadata.create_all(self.engine)
        self.selection = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        self.words = pd.read_csv("../words.csv")["words"].to_list()

    def get_selection(self):
        return self.selection

    def get_words(self, seed):
        random.seed(seed)
        random_words = random.sample(self.words, 45)
        return random_words

    def check_authorization(self, username: str, password: str) -> bool :

        pwd_bytes = password.encode("utf-8")

        user = self.select_username(username)
        if user is None:
            print("There is not a user in the db.")
            return False

        return bcrypt.checkpw(pwd_bytes, user.password)

    def select_username(self, username: str) -> User | None:

        stmt = select(User).where(User.username == username)

        with Session(self.engine) as session:
            user = session.scalars(statement=stmt).first()

        return user if user else None

    def add_user(self, username, password) -> None:
        pwd_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(pwd_bytes, salt)

        with Session(self.engine) as session:
            user = User(
                username=username,
                password=pwd_hash
            )

            session.add(user)
            session.commit()


    def add_achievement(self, username: str, achieved_at: dt.datetime, time: str) -> None:
        with Session(self.engine) as session:
            user = session.query(User).filter_by(username=username).first()
            if user:
                achievement = Achievement(
                    achieved_at=achieved_at,
                    time=time
                )
                user.achievements.append(achievement)
                session.commit()

    def user_achievements(self, username: str):

        with Session(self.engine) as session:
            user = session.query(User).filter_by(username=username).first()
            achievements = { idx : [achievement.achieved_at, achievement.time] for idx, achievement in enumerate(user.achievements)}

            return achievements

