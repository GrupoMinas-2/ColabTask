from kivy.lang.builder import Builder
from kivy.uix.modalview import ModalView
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup

Builder.load_file('dev/app/interface/kvLang/ModalTask.kv')

class ModalTask(ModalView):

    def abrirmodalData(self):
        dp= DatePicker()
        dp.open()
    pass

class DatePicker(Popup):

    pass
