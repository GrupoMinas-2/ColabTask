from kivy.lang.builder import Builder
from kivy.uix.popup import Popup

Builder.load_file('dev/app/interface/kvLang/popupError.kv')

class PopupError(Popup):
    def inserPopupError(self, mensage):
        
        self.ids.contentpopup.text = mensage
        self.open()


    