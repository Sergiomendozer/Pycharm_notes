from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class AnchorLayoutExample(AnchorLayout):
    pass

class Boxlayout(BoxLayout):
    pass
    """def __init__(self,**kwargs):
        super(). __init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)"""

class MainWidget(Widget):
    pass

class lab(App):
    pass

lab().run()