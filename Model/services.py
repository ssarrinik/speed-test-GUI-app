import os

import pandas as pd
import random
from Model.Models import User, Base
from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
import bcrypt


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

    def check_authorization(self, username, password):

        pwd_bytes = password.encode("utf-8")

        user = self.select_username(username)
        if user is None:
            print("There is not a user in the db.")
            return False

        return bcrypt.checkpw(pwd_bytes, user.password.encode("utf-8"))

    def select_username(self, username) -> User | None:

        stmt = select(User).where(User.username == username)

        with Session(self.engine) as session:
            user = session.scalars(statement=stmt).first()

        return user if user else None

    def add_user(self, username, password):
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
