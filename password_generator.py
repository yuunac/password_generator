from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class PasswordGenerator(App):
    def build(self):
        self.window = GridLayout()
        self.window.rows = 3
        self.window.size_hint = (0.5,0.5)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
        Window.size = (450,250)
        
        #casella_testo
        self.input_testo = TextInput(size_hint=(1,0.8),
                                     input_filter="int"
                                     )
        self.window.add_widget(self.input_testo)
        
        #bottone
        self.bottone = Button(text = "Generate",
                              font_size = 25,
                              bold= True,
                              color="#1c2833",
                              background_color=(96, 200, 235, 0.9)
                              )
        self.window.add_widget(self.bottone)
        self.bottone.bind(on_press = self.genera_password)
        
        #etichetta
        self.etichetta = Label(text="",
                               color="#60c8ebeb",
                               font_size="20sp")
        self.window.add_widget(self.etichetta)
        
        return self.window

    #funzione genera_password
    def genera_password(self,instance):
        stringa=""
        try:
            for i in range(int(self.input_testo.text)):
                numero_casuale = random.randint(33,125)
                lettera = chr(numero_casuale)
                stringa += lettera
        except TypeError:
            print("Error on typing")
        self.etichetta.text=f"Generated password: {stringa}"
    
    
    
PasswordGenerator().run()
