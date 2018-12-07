from os import system,name
from services.CarService import CarService
from models.Car import Car
from time import sleep
from datetime import date
import string
from models.ui_methods import print_header, error_handle

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
            if action == "1":
                prompt += " / Skoða bíl"
                print_header(prompt)
                exit_info = ""
                while exit_info == "":
                    registration_num = input("Bílnúmer: ")
                    car_found = self.__CarService.car_find(registration_num)
                    if not car_found:
                        choice = error_handle("Bíll", registration_num)
                        if choice == "1":
                            print_header(prompt)
                            continue
                        elif choice == "2":
                            break
                        elif choice == "3":
                            done = True
                            break
                    system('clear')
                    print_header(prompt)
                    print(car_found)
                    print("="*60)
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
                new_car = new_car.make_car(prompt)
                if type(new_car) != int:
                    print_header(prompt)
                    print("Bíll skráður í kerfið.")
                    sleep(3)
                    self.__CarService.car_register(new_car)
                elif new_car == 1: 
                    done = True
            elif action == "3":
                exit_info = ""
                while exit_info == "":
                    prompt += " / Skoða lausa bíla"
                    print_header(prompt)
                    self.__CarService.get_available_cars(prompt)
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
                    busy_cars_dict = self.__CarService.get_busy_cars(prompt)
                    self.__CarService.print_car_dict(busy_cars_dict)
                    question = input("1.  Skoða fleiri bíla í útleigu\n2.  Tilbaka\n3.  Heim\n")
                    if question == "2":
                        exit_info = "Tilbaka"
                    elif question == "3":
                        exit_info = "Heim"
                        done = True
            else:
                done = True


