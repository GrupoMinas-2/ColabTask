from kivy.lang.builder import Builder

from kivy.uix.screenmanager import Screen

from app.domain.useCases.login_user import usecase_login

from app.interface.widgets.poupError_iten import PopupError

Builder.load_file("dev/app/interface/kvLang/LoginPage.kv")

class LoginPage(Screen):
    
    def do_login(self):
        pass
        email_input = self.ids.inputMail.text
        password_input = self.ids.inpuPassword.text

        self.usecase = usecase_login()

        response = self.usecase.executeLogin(email_input, password_input)

        if response["sucess"]:
            print(response["message"])

            #self.manager.get_screen("homepage").insertNucleos_byUser(self.ids.inputMail.text)
            self.manager.current = "homepage"

        else:
            print("erro", response["message"])
            self.popup= PopupError()
            self.popup.inserPopupError(response["message"])
        
    