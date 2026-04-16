import ttkbootstrap as ttk
import tkinter as tk
from View import constants


class SignIn:
    def __init__(self, root: ttk.Window):
        self.root = root
        self.root.title("Speed Test — Sign In")
        self.root.geometry("800x700")
        self.root.configure(bg=constants.BG)

        frame = tk.Frame(self.root, bg=constants.PANEL, bd=0, highlightthickness=1,
                         highlightbackground=constants.BORDER)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=300)


        tk.Label(frame, text="USERNAME", font=constants.FONT_LABEL, bg=constants.PANEL,
                 fg=constants.MUTED).place(x=20, y=20)

        self.entry_user = tk.Entry(
            frame,
            font=constants.FONT_MONO,
            bg=constants.TEXT_BG,
            fg=constants.TEXT_FG,
            insertbackground=constants.CURSOR,
            relief="flat",
            highlightthickness=1,
            highlightcolor=constants.ACCENT,
            highlightbackground=constants.BORDER,
        )
        self.entry_user.place(x=20, y=42, width=260, height=30)

        tk.Label(frame, text="PASSWORD", font=constants.FONT_LABEL, bg=constants.PANEL,
                 fg=constants.MUTED).place(x=20, y=88)

        self.entry_pass = tk.Entry(
            frame,
            font=constants.FONT_MONO,
            bg=constants.TEXT_BG,
            fg=constants.TEXT_FG,
            insertbackground=constants.CURSOR,
            relief="flat",
            highlightthickness=1,
            highlightcolor=constants.ACCENT,
            highlightbackground=constants.BORDER,
            show="•",
        )
        self.entry_pass.place(x=20, y=110, width=260, height=30)

        self.btn = tk.Button(
            frame,
            text="▶  Sign In",
            font=constants.FONT_TITLE,
            bg=constants.ACCENT,
            fg=constants.BG,
            activebackground=constants.ACCENT,
            activeforeground=constants.BG,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.on_sign_in,
        )
        self.btn.place(x=20, y=166, width=260, height=36)

        self.register = tk.Button(
            frame,
            text="▶  Register",
            font=constants.FONT_TITLE,
            bg=constants.ACCENT,
            fg=constants.BG,
            activebackground=constants.ACCENT,
            activeforeground=constants.BG,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.on_sign_in,
        )
        self.register.place(x=20, y=210, width=260, height=36)

    def bind_login(self, call):
        self.btn.bind("<Button-1>", call)

    def bind_register(self, call):
        self.register.bind("<Button-1>", call)


    def on_sign_in(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()

        return user, pwd

    def destroy_sign_in(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.quit()

    def mainloop(self):
        self.root.mainloop()
