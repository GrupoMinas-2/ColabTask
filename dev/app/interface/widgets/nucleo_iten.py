from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("dev/app/interface/kvLang/Nucleo.kv")

class Nucleo(BoxLayout):

    def __init__( self, titulo, descricao, id_nucleo, **Kwargs ): 
        super().__init__(**Kwargs)
        
        if not titulo.strip():
            titulo = "nome núcleo"
        if not descricao.strip():
            descricao= "descrição"
            
        self.ids.nucleoTitle.text =  titulo
        self.ids.taskDescription.text =  descricao
        self.idnucleo = id_nucleo
        