from Model.services import ModelService
from View.SignIn import SignIn
import ttkbootstrap as ttk

class SignInController:

    def __init__(self, root: ttk.Window):
        self.view = SignIn(root)
        self.model = ModelService()
        self.setup()
        self.current_user = False

    def setup(self):
        self.view.bind_login(self.handle_login)
        self.view.bind_register(self.handle_register)

    def handle_login(self, event):
        username, password = self.view.on_sign_in()
        if self.model.check_authorization(username, password):
            self.view.destroy_sign_in()
            self.current_user = True

    def run_main_loop(self):
        self.view.mainloop()

    def handle_register(self, event):
        username, password = self.view.on_sign_in()

        self.model.add_user(username, password)


