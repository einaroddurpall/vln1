from os import system,name
from services.CarService import CarService
from models.Car import Car
from time import sleep
from datetime import date
import string
from models.Functions import print_header, error_handle

class CarMenu:

    def __init__(self):
        self.__car_service = CarService()
        self.car_menu()

    def car_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma bíl við """
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
                    car_selected = True
                    while car_selected:
                        prompt = "Heimasíða / Bílar / Skoða bíl"
                        system('clear')
                        print_header(prompt)
                        car_found.set_availability(self.__car_service.get_date_dict())
                        print(car_found)
                        print("="*70)
                        choice = input("\n1.  Skoða pantanir\n2.  Leita að öðru bílnúmeri\n3.  Uppfæra upplýsingar bíls\n4.  Afskrá bíl\nt.  Tilbaka\nh.  Heim\n").lower()
                        if choice == "1":
                            print_header(prompt)
                            car_orders = self.__car_service.car_get_history(car_found)
                            if car_orders:
                                for order in car_orders:
                                    print(order)
                                    print()
                            else:
                                print_header(prompt)
                                print("Þessi bíll hefur enga notkunarsögu.")
                            input("Ýttu á enter til að halda áfram: ")
                        elif choice == "2":
                            prompt += " / Leita að öðru bílnúmeri"
                            print_header(prompt)
                            car_selected = False
                        elif choice == "3":
                            prompt += " / Uppfæra upplýsingar bíls"
                            self.__car_service.change_car_info(car_found, False, prompt)
                        elif choice == "4":
                            prompt += " / Afskrá bíl"
                            print_header(prompt)
                            choice = input("Ertu viss?(j/n): ")
                            if choice == "j":
                                self.__car_service.car_delete(car_found)
                                exit_info = "Tilbaka"
                                car_selected = False
                        elif choice == "t" or choice == "h":
                            if choice == "h":
                                done = True
                            exit_info = "Tilbaka"
                            car_selected = False
            elif action == "2":    # Pæling með hætta við þegar maður velur flokk
                prompt += " / Skrá nýjan bíl"
                print_header(prompt)
                car_was_made = self.__car_service.make_car(prompt)
                if type(car_was_made) != str:
                    print_header(prompt)
                    print("Bíll skráður í kerfið.")
                    input('Smelltu á "Enter" til að halda áfram')
                else: 
                    if car_was_made == "h":
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