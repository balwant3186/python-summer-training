#pip install kivy
import kivy

from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):

    def build(self):
        return Button(text='Hello World')


if _name_ == '_main_':
    MyApp().run()
