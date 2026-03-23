import ttkbootstrap as ttk
import tkinter as tk
import constants


class SignIn(ttk.Window):
    def __init__(self):
        super().__init__(themename="cyborg")
        self.title("Speed Test — Sign In")
        self.geometry("800x700")
        self.resizable(False, False)
        self.configure(bg=constants.BG)

        frame = tk.Frame(self, bg=constants.PANEL, bd=0, highlightthickness=1,
                         highlightbackground=constants.BORDER)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=230)


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

    def bind_login(self, call):
        self.btn.bind("<Click>", call)

    def on_sign_in(self):
        user = self.entry_user.get()
        pwd = self.entry_pass.get()

        return user, pwd

    def destroy_sign_in(self):
        self.destroy()

