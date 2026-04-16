import ttkbootstrap as ttk
import tkinter as tk
import View.constants as constants
import datetime as dt

class Board:

    def __init__(self, root: ttk.Window, achievements: dict[int :list[dt.datetime, str]]) -> None:
        self.root = root
        self.previous_tries = []
        self.root.title("Speed Test — Achievements")
        self.root.geometry("800x700")
        self.root.configure(bg=constants.BG)

        for idx, key in enumerate(achievements):
            if idx > 9: break

            date, completion_time = achievements[key]

            # Alternating row background
            row_bg = constants.PANEL if idx % 2 == 0 else constants.PANEL_ALT  # e.g. slightly lighter/darker shade

            # Card frame acts as a styled row container
            card = tk.Frame(
                self.root,
                bg=row_bg,
                padx=16,
                pady=10,
                highlightthickness=1,
                highlightbackground=constants.BORDER,  # subtle border
                highlightcolor=constants.ACCENT,  # glows on focus
            )
            card.grid(column=0, row=idx, columnspan=2, sticky="ew", padx=12, pady=4)
            card.columnconfigure(0, weight=1)
            card.columnconfigure(1, weight=0)

            # Date label — primary, left-aligned
            date_label = tk.Label(
                card,
                text=str(date.strftime("%I:%M %p")),
                font=constants.FONT_LABEL,
                bg=row_bg,
                fg=constants.FG_PRIMARY,  # brighter than MUTED
                anchor="w",
                padx=8,
            )
            date_label.grid(column=0, row=0, sticky="w")

            # Time label — badge-style, right-aligned
            time_label = tk.Label(
                card,
                text=f"Words / min {float(completion_time):.2f}",
                font=constants.FONT_LABEL_SMALL,  # slightly smaller
                bg=constants.ACCENT_SUBTLE,  # soft accent background
                fg=constants.ACCENT,  # accent color text
                padx=10,
                pady=4,
                relief="flat",
                borderwidth=0,
            )
            time_label.grid(column=1, row=0, sticky="e", padx=(8, 0))



    def free_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.quit()

    def mainloop(self):
        self.root.mainloop()