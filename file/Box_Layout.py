from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class Boxlayout(BoxLayout):
    def __init__(self,**kwargs):
        super(). __init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)

class Box_lab(App):
    pass

Box_lab().run()