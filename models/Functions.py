from datetime import date
from os import system
import string
from datetime import timedelta

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

def make_car_type():
    valid_car_types = ["Fólksbíll", "Smábíll","Fimm sæta jeppi","Sjö sæta jeppi","Smárúta"]
    valid_car_type = False
    while valid_car_type is False:
        number = input("Flokkur bíls: \n1.  Fólksbíll\n2.  Smábíll\n3.  Fimm sæta jeppi\n4.  Sjö sæta jeppi\n5.  Smárúta\n6.  Hætta við\n")
        try:
            number = int(number)
            car_type = valid_car_types[number -1]
            return car_type
        except:
            print("Númerið: {} er ekki í listanum, reyndu aftur.".format(number))

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
                    ssn = ""
                    break
            if len(ssn) == lenght_of_number:
                legal_ssn = True
            else:
                print(error_code_str)
        return ssn
    
def check_registration_num(registration_num):
    new_registration_num = ""
    for letter in registration_num:
        if (letter in string.ascii_letters) or (letter in string.digits):
            new_registration_num += letter
    if len(new_registration_num) != 5:
        print("Þetta bílnúmer var ólöglegt, reyndu aftur.")
        return False
    registration_num = new_registration_num.upper()
    if registration_num[0] in string.ascii_letters and registration_num[1] in string.ascii_letters\
    and (registration_num[2] in string.ascii_uppercase or registration_num[2] in string.digits)\
    and registration_num[3] in string.digits and registration_num[4] in string.digits:
        return registration_num
    print("Þetta bílnúmer var ólöglegt, reyndu aftur.")
    return False

def check_input(a_string):
    if a_string.lower() == "h":
        return "heim"
    elif a_string.lower() == "t":
        return "tilbaka"

def make_date_list(date1, date2):
    date_list = []
    date_to_list = date1
    while date_to_list <= date2:
        date_list.append(date_to_list)
        date_to_list += timedelta(days=1)
    return date_list

def pretty_str(number, unit):
    number_str = str(number)
    number_new_str = ""
    for index, letter in enumerate(number_str[::-1]):
        if index % 3 == 0 and index != 0:
            number_new_str += "."
        number_new_str += letter
    return number_new_str[::-1] + " " + unit