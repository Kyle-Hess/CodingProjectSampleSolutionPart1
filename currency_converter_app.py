__author__ = 'Kyle'
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty


class CurrencyConverterApp(App):
    def build(self):
        self.title = "Converter"
        self.root = Builder.load_file('gui.kv')
        return self.root

CurrencyConverterApp().run()