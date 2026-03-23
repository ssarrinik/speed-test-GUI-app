import pandas as pd


class Model:
    def __init__(self):
        self.selection = ["one", "two", "three"]
        self.words = pd.read_csv("words.csv")

    def get_selection(self):
        return self.selection

    def get_words(self):
        random_words = self.words.sample(n=50)
        return random_words["words"].to_list()


