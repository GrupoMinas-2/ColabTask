from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("dev/app/interface/kvLang/Nucleo.kv")

class Nucleo(BoxLayout):
    def __init__( self, titulo='tarefa', descrição='desc',**Kwargs ): 
        if not titulo.strip():
            titulo = "nome núcleo"
        if not descrição.strip():
            descrição= "descrição"

        # atribuit valor a descrição
        super().__init__(**Kwargs)
        self.ids.nucleoTitle.text = titulo
        self.ids.taskDescription.text= descrição

        