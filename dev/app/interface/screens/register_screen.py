from kivy.uix.screenmanager import Screen
from app.domain.useCases.register_user import useCase_registerUser

class RegisterPage(Screen): 

    def createAcount(self): 
        email_input = self.ids.inputMail.text
        name_input = self.ids.inputNameUser.text
        password_input = self.ids.inputPassword

        use_case= useCase_registerUser()

        response = use_case.executeRegister(
                                email= email_input,
                                name= name_input,
                                pasword= password_input
                            )
        
        if response["success"]:
            print("Conta criada com sucesso!")
            self.manager.current = "loginpage"

        else:
            print("erro", response["response"])
        

