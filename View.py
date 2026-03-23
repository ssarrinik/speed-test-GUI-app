import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class View(ttk.Window):

    def __init__(self):
        super().__init__()
        self.geometry("800x700")
        self.title("Speed Test")

        self.grid_rowconfigure(0)
        self.grid_columnconfigure(1)

        self.listbox = tk.Listbox(self, height=24)
        self.listbox.grid(row=1, column=0, rowspan=2, padx=10)

        self.label = ttk.Label(self, text="Nothing Selected")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.text_title = ttk.Label(self, text="START HERE WRITING <PRESS ENTER TO START>")
        self.text_title.grid(row=0, column=1, pady=5, padx=5)

        self.placeholder = ttk.Text(self, height=12, width=50)
        self.placeholder.grid(row=1, column=1, padx=5, pady=5, rowspan=1)

        self.text = ttk.Text(self, height=11, width=50)
        self.text.grid(row=2, column=1, padx=5, pady=5, rowspan=1)

    def set_label_text(self, text):
        self.label.config(text=text)

    def set_title_text(self, text):
        self.text_title.config(text=text)

    def bind_listbox(self, call):
        self.listbox.bind("<<ListboxSelect>>", call)

    def bind_start_title(self, call):
        self.bind("<Key>", call)

    def get_text(self):
        return self.text.get("1.0", "end-1c")


    def add_items_in_list(self, items):
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, item)


    def insert_a_word(self, word):
        self.placeholder.insert("0.0", word)
        self.placeholder.mark_set("insert" ,"0.0")
        self.placeholder.focus()


    def disable_placeholder_window(self):
        self.placeholder.config(state="disabled")
