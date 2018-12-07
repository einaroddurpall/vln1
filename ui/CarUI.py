from os import system,name
from services.CarService import CarService
from models.Car import Car, make_car_type
from time import sleep
from datetime import date
import string


def print_header(prompt=""):
    """ Hreinsar terminal og prentar út header með slóð """
    system('clear')
    print("Heimasíða", end="")
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

def search_for_spacific_kind(a_dict):
    """Function that asks user if he wan't to find
    info about specific car type and dose so"""
    question = input("Viltu leita af ákveðnari tegund (j/n)? ")
    if question == "j":
        car_type = make_car_type()
        if car_type in a_dict.keys():
            print("\n{}:".format(car_type))
            print("="*60)
            for car_info in a_dict[car_type]:
                print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
            print("="*60)
            return False
        else:
            print("Enginn bíll laus í þessari bílategund á þessum tíma")
    return True

def Print_out_info_for_all_car_types(a_dict):
    for key,val in a_dict.items():
                        print("\n{}:".format(key))
                        print("="*60)
                        for car_info in val:
                            print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
                        print("="*60)


class CarMenu:

    def __init__(self, prompt):
        self.__CarService = CarService()
        self.__prompt = prompt
        self.car_menu()

    def get_car_info_in_dict(self):
        print_header(self.__prompt)
        while True:
            try:
                date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                return self.__CarService.get_busy_cars(date1, date2)
            except: 
                print("Vinsamlegast sláðu inn gilda dagsetningu")

    def car_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma bíl við """
        
        print_header(self.__prompt)
        action = input("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu\n")
        if action == "1":
            self.__prompt += " / Skoða bíl"
            print_header(self.__prompt)
            exit_info = ''
            while exit_info == '':
                registration_num = input("Bílnúmer: ")
                car_found_info = self.__CarService.car_find(registration_num)
                if car_found_info:
                    pass
                else:
                    svar = input("Bill fannst ekki, reyna aftur (j/n)?")
                    if svar.lower() == 'j':
                        continue
                    else:
                        break
                system('clear')
                print_header(self.__prompt)
                print(car_found_info)
                print()
                question = input("Leita að öðru bílnúmer (j/n)?")
                if question.lower() == "j":
                    continue
                exit_info = input("Sláðu inn eitthvað til að fara heim: ")
            pass

        elif action == "2":
            self.__prompt += " / Skrá nýjan bíl"
            print_header(self.__prompt)
            new_car = Car()
            new_car = new_car.make_car()
            system('clear')
            print_header(self.__prompt)
            print("Bíll skráður í kerfið")
            sleep(3)
            self.__CarService.car_register(new_car)

        elif action == "3":
            self.__prompt += " / Skoða bíla í leigu"
            car_busy_dict = self.get_car_info_in_dict()
            all_car_dict = self.__CarService.make_all_cars_dict()
            delet_key_list = []
            for key in all_car_dict:
                for car in all_car_dict[key]:
                    if car in car_busy_dict[key]:
                        all_car_dict[key].remove(car)
                        if all_car_dict[key] == []:
                            delet_key_list.append(key)
            for key in delet_key_list:
                del all_car_dict[key]
            if all_car_dict:
                statement = search_for_spacific_kind(all_car_dict)
                if statement:
                        Print_out_info_for_all_car_types(all_car_dict)
            else:
                print("Enginn laus bíll á þessum tíma")
            exit_info = input("Sláðu inn eitthvað til að fara heim: ")

        elif action == "4":
            self.__prompt += " / Skoða bíla í útleigu"
            car_info_dict = self.get_car_info_in_dict()

            if car_info_dict:
                statement = search_for_spacific_kind(car_info_dict)
                if statement:
                    Print_out_info_for_all_car_types(car_info_dict)
            else: 
                print("Enginn bíll í útleigu á þessum tíma")
            exit_info = input("Sláðu inn eitthvað til að fara heim: ")
        