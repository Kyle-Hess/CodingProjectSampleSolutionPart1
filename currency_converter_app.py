__author__ = 'Kyle'
from currency import get_all_details
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.config import Config
from kivy.uix.textinput import TextInput

Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '700')

COUNTRIES = {'United States': "USD", 'Belgium': "EUR", 'Cyprus': "EUR", 'Japan': "JPY"}



class CurrencyConverterApp(App):
    current_country = StringProperty()
    country_codes = ListProperty()

    def build(self):
        self.title = "Converter"
        self.root = Builder.load_file('gui.kv')
        # spiner stuff
        self.country_codes = sorted(COUNTRIES.keys())
        self.current_country = self.country_codes[0]
        #####

        return self.root

    def change_country(self, country_code):
        """ handle change of spinner selection, output result to label widget """
        self.root.ids.trip_location.text = COUNTRIES[country_code]
        print("changed to", country_code)

    def on_enter(instance, value):
        print('User pressed enter in', instance)

    inputamount = TextInput(text='', multiline=False)
    inputamount.bind(on_text_validate=on_enter)
    
    #def __init__(self, trip_detais):
        #pass

    def other(self):
        country_name = input("Enter Country name:").title()
        print(get_all_details(country_name))
        pass

    def convert(self):
        value = float(self.root.ids.input_amount.text)
        result = value

    def date(self):
        pass

CurrencyConverterApp().run()


