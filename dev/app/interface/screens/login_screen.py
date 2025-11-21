from kivy.uix.screenmanager import Screen
#from app.domain.use_cases.login_user import LoginUserUseCase

class LoginPage(Screen):
    def do_login(self):
        email = self.ids.email_input.text
        senha = self.ids.password_input.text
    
    #    try:
    #        user = LoginUserUseCase().execute(email, senha)
    #        self.ids.status_label.text = f"Bem-vindo, {user.name}!"
    #    except Exception as e:
    #        self.ids.status_label.text = str(e)
    #pass