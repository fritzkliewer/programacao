import kivy
kivy.require('2.3.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.clock import Clock

# ...

def on_checkbox_active(checkbox, value):
    if value:
        print('The checkbox', checkbox, 'is active')
    else:
        print('The checkbox', checkbox, 'is inactive')


class Controles(Widget):
    def start_progress(self, instance):
        Clock.schedule_interval(self.update_progress, 1/25)
                       
    def update_progress(self, dt):
        if self.pb.value >= 100:
            self.popup.dismiss()
            return False
        self.pb.value += 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lbl = Label(text='Accept Terms', pos=(20, 100))
        self.add_widget(self.lbl)
        self.chk = CheckBox(pos=(150, 100), active=False)
        self.chk.bind(active=on_checkbox_active)
        self.add_widget(self.chk)
        self.bt = Button(pos=(150, 200),size=(160, 50),text='SALVAR')
       
        def on_press(inst):
            print('Button pressed')
            
            layout = GridLayout(cols = 1, padding = 10)
            self.popup = Popup(title ='Salvar',content = layout) 
            self.pb = ProgressBar(max=100, value=0, size_hint=(1, None), height=30)
            layout.add_widget(self.pb)
            popupLabel = Label(text = "Gostaria de salvar?")
            layout.add_widget(popupLabel)
            botaosim = Button(text = "Sim")
            
            botaosim.bind(on_press = self.start_progress) 
            layout.add_widget(botaosim)   
            closeButton = Button(text = "Não")
            closeButton.bind(on_press = self.popup.dismiss) 
            layout.add_widget(closeButton)                    
            self.popup.open()                

        self.bt.bind(on_press=on_press)
        self.add_widget(self.bt)

class MyApp(App):

    def build(self):        
        return Controles()


if __name__ == '__main__':
    MyApp().run()