from View.SignIn import SignIn


class SignInController:

    def __init__(self, view: SignIn):
        self.view = view

    def setup_login(self):
        self.view.bind_login(self.handle_login)


    def handle_login(self):
        username, password = self.view.on_sign_in()
        print(username, password)

    def run_main_loop(self):
        self.view.mainloop()