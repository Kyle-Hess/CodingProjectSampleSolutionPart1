__author__ = 'Kyle'
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty

COUNTRIES = {'USD': "United States", 'BGM': "Belgium", 'CYP': "Cyprus", 'JPY': "Japan"}

class CurrencyConverterApp(App):
    current_country = StringProperty()
    country_codes = ListProperty()

    def build(self):
        self.title = "Converter"
        self.root = Builder.load_file('gui.kv')
        #spner stuff
        self.country_codes = sorted(COUNTRIES.keys())
        self.current_country = self.country_codes[0]
        #####
        return self.root

    def change_country(self, country_code):
        """ handle change of spinner selection, output result to label widget """
        self.root.ids.output_label.text = COUNTRIES[country_code]
        print ("changed to", country_code)

CurrencyConverterApp().run()