from os import system,name
from time import sleep
from datetime import date
import string
from services.CarService import CarService
from models.Car import Car
from models.Functions import print_header, error_handle

class CarMenu:

    def __init__(self):
        self.__car_service = CarService()
        self.car_menu()

    def car_menu(self):
        """ Hér eru allar aðgerðir undir "Bílar" framkvæmdar sem skiptast í fernt.
            1. Skoða bíl, hér þarf að setja inn bílnúmer sem CarService klasinn tekur, athugar hvort það sé í kerfinu og skilar bíl.
               Þegar bíll er valinn þá er hægt að framkvæma fjórar aðgerðir á honum.
                1.1. Skoða pantanir, þar er hægt að skoða allar þær pantanir sem hafa verið gerðar á þeim bíl.
                1.2. Leita að öðru bílnúmeri
                1.3. Uppfæra upplýsingar um bíl, hér er hægt að breyta undirtegund, skiptingu og hvað bíllinn er keyrður mikið.
                     Þegar upplýsingarnar hafa breyttar þá uppfærast öll skjöl sem bíllinn er tengdur við. (Sjá ChangeService klasann)
                1.4. Afskrá bíl, hér er bíllinn afskráður úr kerfinu og allar þær pantarnir sem hann var með fá sjálfkrafa nýjan bíl
                     (sjá ChangeService klasann)
            2. Skrá nýjan bíl, sjá make_car fallið í CarService.
            3. Skoða lausa bíla, sjá get_available_cars fallið í CarService klasanum.
            4. Skoða bíla í útleigu, sjá get_busy_cars fallið í CarService klasanum."""
        done = False
        while not done:
            prompt = "Heimasíða / Bílar"
            print_header(prompt)
            action = input("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu\nh.  Heim\n").lower()
            if action == "1":
                prompt += " / Skoða bíl"
                print_header(prompt)
                exit_info = ""
                while exit_info == "":
                    registration_num = input("Bílnúmer: ")
                    if registration_num == "t" or registration_num == "h":
                        if registration_num == "h":
                            done = True
                        break
                    car_found, legal_reg_num = self.__car_service.car_find(registration_num)
                    if not car_found:
                        if not legal_reg_num:
                            choice = input('1.  Reyna aftur\nt.  Tilbaka\nh.  Heim\n')
                        else:
                            choice = error_handle("Bíllinn", registration_num)
                        if choice == "1":
                            print_header(prompt)
                            continue
                        elif choice == "t" or choice == "h":
                            if choice == "h":
                                done = True
                            break
                    exit_info, done = self.view_car(car_found)
            elif action == "2":
                prompt += " / Skrá nýjan bíl"
                print_header(prompt)
                new_car = self.__car_service.make_car(prompt)
                if type(new_car) == Car:
                    exit_info, done = self.view_car(new_car)
                else: 
                    if new_car == "h":
                        done = True
            elif action == "3":
                exit_info = ""
                prompt += " / Skoða lausa bíla"
                print_header(prompt)
                while exit_info == "":
                    go_home = self.__car_service.get_available_cars(prompt)
                    if go_home != True:
                        choice = ""
                        while choice != "1":
                            choice = input("1.  Skoða fleiri lausa bíla\nt.  Tilbaka\nh.  Heim\n").lower()
                            if choice == "t" or choice == "h":
                                if choice == "h":
                                    done = True
                                exit_info = "Tilbaka"
                                break
                            print_header(prompt)
                    else:
                        exit_info = "Tilbaka"
            elif action == "4":
                exit_info = ""
                print_header(prompt)
                while exit_info == "":
                    prompt += " / Skoða bíla í útleigu"
                    busy_cars_dict = self.__car_service.get_busy_cars(prompt)
                    go_home = self.__car_service.print_car_dict(busy_cars_dict)
                    if go_home != True:
                        choice = ""
                        while choice != "1":
                            choice = input("1.  Skoða fleiri bíla í útleigu\nt.  Tilbaka\nh.  Heim\n")
                            if choice == "t" or choice == "h":
                                if choice == "h":
                                    done = True
                                exit_info = "Tilbaka"
                                break
                            print_header(prompt)
                    else:
                        exit_info = "Tilbaka"
            elif action == "h":
                done = True




    def view_car(self, car):
        car_selected = True
        while car_selected:
            prompt = "Heimasíða / Bílar / Skoða bíl"
            system('clear')
            print_header(prompt)
            car.set_availability(self.__car_service.get_date_dict())
            print(car)
            print("="*70)
            choice = input("\n1.  Skoða pantanir\n2.  Uppfæra upplýsingar bíls\n3.  Afskrá bíl\nt.  Tilbaka\nh.  Heim\n").lower()
            if choice == "1":
                print_header(prompt)
                car_orders = self.__car_service.car_get_history(car)
                if car_orders:
                    for order in car_orders:
                        print(order)
                        print()
                else:
                    print_header(prompt)
                    print("Þessi bíll hefur enga notkunarsögu.")
                input('Ýttu á "Enter" til að halda áfram: ')
            elif choice == "2":
                prompt += " / Uppfæra upplýsingar bíls"
                self.__car_service.change_car_info(car, False, prompt)
            elif choice == "3":
                prompt += " / Afskrá bíl"
                print_header(prompt)
                choice = input("Ertu viss?(j/n): ")
                if choice == "j":
                    self.__car_service.car_delete(car)
                    return "Tilbaka", False
            elif choice == "t":
                return "Tilbaka", False
            elif choice == "h":
                return "Heim" , True
                

