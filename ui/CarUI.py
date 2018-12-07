from os import system,name
from services.CarService import CarService
from models.Car import Car
from time import sleep
from datetime import date
import string
from models.ui_methods import print_header
# from models.ui_methods import make_date

# def search_for_spacific_kind(a_dict):
#     """Function that asks user if he wants to find
#     info about specific car type and does so"""
#     question = input("Viltu leita af ákveðnari tegund (j/n)? ")
#     if question == "j":
#         car_type = make_car_type()              #Key er tegund bílsins bæta við verði við hliðin á tegundinni carservice get_car_price
#         if car_type in a_dict.keys():
#             print("\n{}:".format(car_type))
#             print("="*60)
#             for car_info in a_dict[car_type]:
#                 print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
#             print("="*60)
#             return False
#         else:
#             print("Enginn bíll laus í þessari bílategund á þessum tíma")
#     return True

# def print_out_info_for_all_car_types(a_dict):
#     for key,val in a_dict.items():
#         print("\n{}:".format(key))    #Key er tegund bílsins bæta við verði við hliðin á tegundinni
#         print("="*60)
#         for car_info in val:
#             print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
#         print("="*60)

class CarMenu:

    def __init__(self):
        self.__CarService = CarService()
        self.car_menu()

    def car_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma bíl við """
        done = False
        while not done:
            prompt = "Heimasíða / Bílar"
            print_header(prompt)
            action = input("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu\n5.  Heim\n")
            if action == "1":  #Tilbúið
                prompt += " / Skoða bíl"
                print_header(prompt)
                exit_info = ""
                while exit_info == "":
                    car_found = self.__CarService.car_find(input("Bílnúmer: "))
                    if not car_found:
                        question = input("Bíll fannst ekki, reyna aftur (j/n)? ")
                        if question.lower() == 'j':
                            print_header(prompt)
                            continue
                        else:
                            break
                    system('clear')
                    print_header(prompt)
                    print(car_found)
                    question = input("\n1.  Leita að öðru bílnúmeri\n2.  Tilbaka\n3.  Heim\n")
                    if question == "2":
                        exit_info = "Tilbaka"
                    elif question == "3":
                        exit_info = "Heim"
                        done = True
            elif action == "2":
                prompt += " / Skrá nýjan bíl"
                print_header(prompt)
                new_car = Car()
                new_car = new_car.make_car()
                if new_car:
                    print_header(prompt)
                    print("Bíll skráður í kerfið.")
                    sleep(3)
                    self.__CarService.car_register(new_car)
            elif action == "3":
                exit_info = ""
                while exit_info == "":
                    prompt += " / Skoða lausa bíla"
                    print_header(prompt)
                    self.__CarService.get_available_cars()
                    question = input("1.  Skoða fleiri lausa bíla\n2.  Tilbaka\n3.  Heim\n")
                    if question == "2":
                        exit_info = "Tilbaka"
                    elif question == "3":
                        exit_info = "Heim"
                        done = True
            elif action == "4":
                exit_info = ""
                while exit_info == "":
                    prompt += " / Skoða bíla í útleigu"
                    print_header(prompt)
                    busy_cars_dict = self.__CarService.get_busy_cars()
                    self.__CarService.print_car_dict(busy_cars_dict)
                    question = input("1.  Skoða fleiri bíla í útleigu\n2.  Tilbaka\n3.  Heim\n")
                    if question == "2":
                        exit_info = "Tilbaka"
                    elif question == "3":
                        exit_info = "Heim"
                        done = True
            else:
                done = True