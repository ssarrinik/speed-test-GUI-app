from Core.SignInController import SignInController
from Core.GameController import GameController
import ttkbootstrap as ttk
import pymysql


if __name__ == "__main__":
    root = ttk.Window(themename="cyborg")

    controller = SignInController(root)
    controller.run_main_loop()

    if controller.current_user:
        controller = GameController(root)
        controller.setup()
        controller.view.mainloop()