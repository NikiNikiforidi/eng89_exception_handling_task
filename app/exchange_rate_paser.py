import json

class Exchange_rate:
    def __init__(self, currency_code):
        self.list = [] #Create an empty list
        self.currency_code = currency_code.upper() #Save user input and make it uppser case
        self.exchange_rates = json.load(open("exchange_rates.json", "rt")) # load and open the json file


        for key, value in self.exchange_rates['rates'].items(): # Open rates key in json dict and itterate through keys, items
            if key == self.currency_code:
                self.list = (f"The currency codes is {key} and the rate is {value}")
                print(self.list)


Exchange_rate(input("Please enter the currency code you would like to review: ").strip())
