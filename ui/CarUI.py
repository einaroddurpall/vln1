from os import system,name
from services.CarService import CarService
from models.Car import Car
from time import sleep
from datetime import date
import string
from models.methods import print_header, error_handle

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
            action = input("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu\n5.  Heim\n")
            if action == "1":
                prompt += " / Skoða bíl"
                print_header(prompt)
                exit_info = ""
                while exit_info == "":
                    registration_num = input("Bílnúmer: ")
                    car_found = self.__car_service.car_find(registration_num)
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
                    car_selected = True
                    while car_selected:
                        system('clear')
                        print_header(prompt)
                        print(car_found)
                        print("="*60)
                        question = input("\n1.  Skoða pantanir\n2.  Leita að öðru bílnúmeri\n3.  Uppfæra upplýsingar bíls\n4.  Afskrá bíl\n5.  Tilbaka\n6.  Heim\n")
                        if question == "1":
                            car_orders = self.__car_service.car_get_history(car_found)
                            if car_orders:
                                for order in car_orders:
                                    print(order)
                            else:
                                print("Þessi bíll hefur enga notkunarsögu.")
                            input("Ýttu á enter til að halda áfram: ")
                        elif question == "3":
                            self.__car_service.change_car_info(car_found, False)
                            
                        elif question == "4":
                            prompt += " / Afskrá bíl"
                            print_header(prompt)
                            choice = input("Ertu viss?(j/n): ")
                            if choice == "j":
                                self.__car_service.car_delete(car_found)
                                exit_info = "Tilbaka"
                                car_selected = False
                        elif question == "5":
                            exit_info = "Tilbaka"
                            car_selected = False
                        elif question == "6":
                            exit_info = "Heim"
                            car_selected = False
                            done = True
            elif action == "2":
                prompt += " / Skrá nýjan bíl"
                print_header(prompt)
                car_was_made = self.__car_service.make_car()
                if car_was_made:
                    print_header(prompt)
                    print("Bíll skráður í kerfið.")
                    sleep(3)
                elif car_was_made == 1: 
                    done = True
            elif action == "3":
                exit_info = ""
                prompt += " / Skoða lausa bíla"
                while exit_info == "":
                    print_header(prompt)
                    go_home = self.__car_service.get_available_cars(prompt)
                    if go_home != True:
                        question = input("1.  Skoða fleiri lausa bíla\n2.  Tilbaka\n3.  Heim\n")
                        if question == "2":
                            exit_info = "Tilbaka"
                        elif question == "3":
                            exit_info = "Heim"
                            done = True
                    else:
                        exit_info = "Tilbaka"
            elif action == "4":
                exit_info = ""
                while exit_info == "":
                    prompt += " / Skoða bíla í útleigu"
                    print_header(prompt)
                    busy_cars_dict = self.__car_service.get_busy_cars(prompt)
                    go_home = self.__car_service.print_car_dict(busy_cars_dict)
                    if go_home != True:
                        question = input("1.  Skoða fleiri bíla í útleigu\n2.  Tilbaka\n3.  Heim\n")
                        if question == "2":
                            exit_info = "Tilbaka"
                        elif question == "3":
                            exit_info = "Heim"
                            done = True
                    else:
                        exit_info = "Hilmar er fáviti"
            else:
                done = True