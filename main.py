from Core.SignInController import SignInController
from Core.GameController import GameController, BoardController
import ttkbootstrap as ttk



if __name__ == "__main__":
    root = ttk.Window(themename="cyborg")

    controller = SignInController(root)
    controller.run_main_loop()

    while controller.current_user:
        controller = GameController(root, controller.current_user)
        controller.setup()
        controller.run_main_loop()

        if not controller.current_user:
            break

        controller = BoardController(root, controller.current_user)
        controller.run_main_loop()
