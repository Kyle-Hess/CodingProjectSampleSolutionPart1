__author__ = 'Kyle'
from currency import get_all_details, convert
from trip import Country, Details
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.textinput import TextInput

# sets the width and height of the window
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '700')

# COUNTRIES = get_all_details
config_dict = {}


# gets the home country from config
def get_home():
    with open("config.txt", 'r', encoding="utf8") as file:
        return file.readline().strip()


# appends the country name to config_dict which id linked to get_all_details
def config_file():
    config_dict = []
    with open("config.txt", 'r', encoding="utf8") as file:
        for line in file:
            items = line.strip().split(',')
            config_dict.append(items[0])
    return config_dict


# creates spinner with the countries in the config.txt
def Spinner():
    spinner_dict = []
    with open("config.txt", 'r', encoding="utf8") as file:
        file.readline()
        for line in file:
            items = line.strip().split(',')
            spinner_dict.append(items[0])
    return spinner_dict


class CurrencyConverterApp(App):
    spinner_countries = Spinner()
    home_country = get_home()
    # conversion = convert()
    trip_location = Spinner()
    # target_amount = convert_to_home()
    # from_home = convert_from_home()
    # to_home = convert_to_home()

    # builds the main gui
    def build(self):
        self.title = "Converter"
        self.root = Builder.load_file('gui.kv')
        self.spinner_countries = Spinner()
        # self.trip_location = Spinner()

        # spiner stuff
        # self.country_codes = sorted(COUNTRIES)
        # self.current_country = self.country_codes[0]
        #####

        return self.root

        # def change_country(self, Spinner):
        """ handle change of spinner selection, output result to label widget """
        # self.root.ids.trip_location.text = config_dict[Spinner()]
        # print("changed to", Spinner())

    '''
    #gets the home country from config.txt to display
    def get_home(self):
        with open("config.txt", 'r', encoding="utf8") as file:
                return file.readline().strip()
    '''

    def change_country(self, current_country):
        self.root.ids.trip_location.text = 'current Location: \n {}', Spinner()  # .format(current_country)
        pass

    # tried to get the current country from selected country in the spinner
    def get_country_details(self, Spinner):
        selected = Spinner()

    def convert_to_home(self, target_amount, home_country, target_country):
        # dont know how to reciece the inputed amount and put it in the the function

        code1 = target_country
        amount = target_amount
        code2 = home_country
        target_amount = ''
        conversion = convert(amount, code1, code2)

        # get selected country = ''
        # get the inputed amount from target_amount
        # get selected countries code
        # get home countries code
        # put the amount and codes back into convert function
        # output result in home_amount (kivy)
        # update Satus (USD to AUD)
        pass

    def convert_from_home(self, get_home):
        #   get selected country = home country (australia)
        # get the inputed amount from home_amount
        # get home country code
        # get selected country code
        # put the amount and codes back into convert function
        # output result in target_amount (kivy)
        # update Satus (AUD to USD)
        # updates status
        pass

    # def __init__(self, trip_detais):
    # pass

    # gets the start and end dates from the config and shows the current date(in kivy)
    def get_dates(self):
        dates = []
        file = open("config.txt", "r", encoding="utf8")
        for line in file:
            if dates in line:
                parts = line.split(',')
                country = parts[0]
                start = parts[1]
                end = parts[2].rstrip()
         #return (country, start, end)
        pass


        # self.root.ids.today_date.text = Details()


CurrencyConverterApp().run()

# convert home
# convert other country
# get current country dte
