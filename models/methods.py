from datetime import date
from os import system
import string

# class UiMethods:
#     def __init__(self)
def print_header(prompt=""):
        """ Hreinsar terminal og prentar út header með slóð """
        system('clear')
        print(prompt)
        print("="*60)

def make_date(a_date):
    new_string = ""
    for letter in a_date:
        if letter in string.digits:
            new_string += letter
    day = new_string[:2]
    month = new_string[2:4]
    year = new_string[4:]
    return date(int(year), int(month), int(day))

def error_handle(search, search_input):
        choice = input('{}: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\n2.  Tilbaka\n3.  Heim\n'.format(search, search_input))
        return choice

def make_number(lenght_of_number, input_string, error_code_str):
        legal_ssn = False
        while not legal_ssn:
            inp = input(input_string)
            ssn = ""
            for letter in inp:
                try:
                    int(letter)
                    ssn += letter
                except:
                    print(error_code_str)
                    continue
            if len(ssn) == lenght_of_number:
                legal_ssn = True
            else:
                print(error_code_str)
        return ssn

def check_input(a_string):
    if a_string.lower() == "h":
        return "heim"
    elif a_string.lower() == "t":
        return "tilbaka"