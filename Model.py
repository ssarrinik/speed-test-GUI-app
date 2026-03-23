import pandas as pd
import random

class Model:
    def __init__(self):
        self.selection = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        self.words = pd.read_csv("words.csv")["words"].to_list()

    def get_selection(self):
        return self.selection

    def get_words(self, seed):
        random.seed(seed)
        random_words = random.sample(self.words, 45)
        return random_words
