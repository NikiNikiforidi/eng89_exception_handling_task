# TASK, working with files exception handling

### user story: as a user I would like to be able to enter country currency code and find out the exchange rate
-Create a package with setup.py
- Create file called exchange_rate_paser.py
- Create a class
- Read data from attached file(exchange_rates.json)
-print country currency code with matching exchange rate
 - Expected outcome GBP exchange rate is 0.89275 

- --------------------------------------------------------------------
**In app directory**
- `__init__.py`and `exchange_rates.json` files exist.
- Created `exchange_rate_paser.py` 
```
# exchange_rate_paser file
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


```
- In normal directory added `setup.py` and `program.py`
```
# program file

from app.exchange_rate_paser import Exchange_rate

Exchange_rate(input("Please enter the currency code you would like to review: ").strip())

```