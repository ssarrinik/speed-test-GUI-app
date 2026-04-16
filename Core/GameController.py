import time
from Model.services import ModelService
from View.board import Board
from View.gameui import View
import datetime as dt

class GameController:

    def __init__(self, root, username: str):
        self.root = root
        self.view = View(root)
        self.model = ModelService()
        self.username = username
        self.start_time = None
        self.words = None

    def setup(self):
        items = self.model.get_selection()
        self.view.add_items_in_list(items)

        self.view.bind_listbox(self.handle_selection)
        self.view.bind_start_title(self.handle_label_start)
        self.view.bind_achievements(self.handle_achievements)

        self.words = self.model.get_words(45)
        for word in self.words:
            self.view.insert_a_word(word + " ")

        self.words.reverse()
        self.view.disable_placeholder_window()


    def handle_selection(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.view.set_label_text(f"{event.widget.get(index)} selected!")

            self.view.enable_placeholder_window()
            self.view.clear_placeholder_text()
            self.words = self.model.get_words(45 + index)
            for word in self.words:
                self.view.insert_a_word(word + " ")
            self.words.reverse()
            self.view.disable_placeholder_window()

    def handle_label_start(self, event):
        if not self.start_time:
            self.start_time = time.time()
            self.view.set_title_text("WE STARTED TO COUNT!")

        if event.char == " ":
            text = self.view.get_text()

            current_text = list(filter(self.filter_unwanted_chars, text.split(" ")))

            print(current_text)
            size = len(self.words) if len(self.words) < len(current_text) else len(current_text)
            current_text = current_text[0:size]


            if current_text == self.words:
                words_per_min = (len(self.words) / (time.time() - self.start_time)) * 60
                self.view.set_title_text(f"SUCCESS WITH TIME {words_per_min: .2f}")
                self.model.add_achievement(self.username, dt.datetime.now(), words_per_min)

            elif current_text != self.words[0: len(current_text)]:
                self.view.set_title_text(f"YOU MADE A MISTAKE")
            else:
                self.view.set_title_text("WE STARTED TO COUNT!")


    def run_main_loop(self):
        self.view.mainloop()

    def filter_unwanted_chars(self, word):
        return word != ' ' and word != '' and word != '\n'


    def handle_achievements(self, event):
        #katastrofi game view kai orismos tou achievement view

        self.view.destroy_game_ui()
        achievements = self.model.user_achievements(self.username)
        print(achievements)

        self.view = Board(self.root, achievements)
        self.view.mainloop()

        self.view = View(self.root)
