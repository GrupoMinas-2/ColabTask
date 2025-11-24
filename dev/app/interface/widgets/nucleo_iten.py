from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from app.domain.useCases.create_nucleo import useCase_createNucleo

Builder.load_file("dev/app/interface/kvLang/Nucleo.kv")

class Nucleo(BoxLayout):
    def __init__( self, titulo='tarefa', descrição='desc',**Kwargs ): 
        super().__init__(**Kwargs)
        
        if not titulo.strip():
            titulo = "nome núcleo"
        if not descrição.strip():
            descrição= "descrição"

        self.ids.nucleoTitle.text = titulo
        self.ids.taskDescription.text= descrição

        self.use_case= useCase_createNucleo()
        result= self.use_case.executeCreation(titulo, descrição)

        if result["sucess"]:
            print(result["message"])
        else:
            print("Nucleo não foi criado!")
        