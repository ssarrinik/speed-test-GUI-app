import time
from Model import Model
from View import  View


class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.start_time = None
        self.words = None


    def setup(self):
        items = self.model.get_selection()
        self.view.add_items_in_list(items)

        self.view.bind_listbox(self.handle_selection)
        self.view.bind_start_title(self.handle_label_start)

        self.words = self.model.get_words()
        for word in self.words:
            self.view.insert_a_word(word + " ")

        self.words.reverse()
        self.view.disable_placeholder_window()

    def change_label_start(self):
        pass

    def handle_selection(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.view.set_label_text(f"{event.widget.get(index)} selected!")
            event.widget.get(index)

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
            elif current_text != self.words[0: len(current_text)]:
                self.view.set_title_text(f"YOU MADE A MISTAKE")
            else:
                self.view.set_title_text("WE STARTED TO COUNT!")


    def calculate_speed(self):
        pass

    def run_main_loop(self):
        self.view.mainloop()

    def filter_unwanted_chars(self, word):
        return word != ' ' and word != '' and word != '\n'


controller = Controller(View(), Model())
controller.setup()
controller.run_main_loop()

