from datetime import date
from os import system
import string

# class UiMethods:
#     def __init__(self)
def print_header(prompt=""):
        """ Hreinsar terminal og prentar út header með slóð """
        system('clear')
        print(prompt)
        print("="*40)

def make_date(a_date):
    new_string = ""
    for letter in a_date:
        if letter in string.digits:
            new_string += letter
    day = new_string[:2]
    month = new_string[2:4]
    year = new_string[4:]
    return date(int(year), int(month), int(day))