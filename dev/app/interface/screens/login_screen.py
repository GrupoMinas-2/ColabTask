from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen

from app.domain.useCases.login_user import usecase_login

from app.interface.widgets.poupError_iten import PopupError

Builder.load_file("dev/app/interface/kvLang/LoginPage.kv")

class LoginPage(Screen):
    
    def do_login(self):
        email_input = self.ids.inputMail.text
        password_input = self.ids.inpuPassword.text

        self.usecase = usecase_login()

        response = self.usecase.executeLogin(email_input, password_input)

        if response["sucess"]:
            print(response["message"], response["iduser"])
            
            self.manager.get_screen("homepage").inicializate_Session(response["iduser"])

            self.manager.get_screen("homepage").searchNucleos_byUser(response["iduser"])

            self.manager.current = "homepage"

        else:
            print("erro", response["message"])
            self.popup= PopupError()
            self.popup.inserPopupError(response["message"])
        
    def test_metod(self):
        self.manager.get_screen("homepage").searchNucleos_byUser(3)
        self.manager.current = "homepage"

    