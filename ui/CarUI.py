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
            1. 
                1.1. 
                1.2. 
                1.3. 
                1.4. 



            2. 
            3. 
            4. Skoða bíla í útleigu, sjá get_busy_cars fallið í CarService klasanum."""
        done = False
        while not done:
            prompt = "Heimasíða / Bílar"
            print_header(prompt)
            action = input("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu\nh.  Heim\n").lower()
            #Skoða bíl, hér þarf að setja inn bílnúmer sem CarService klasinn tekur, athugar hvort það sé í kerfinu og skilar bíl.
            #Þegar bíll er valinn þá er hægt að framkvæma fjórar aðgerðir á honum.
            if action == "1":
                prompt += " / Skoða bíl"
                print_header(prompt)
                exit_info = ""
                while exit_info == "":
                    registration_num = input("Bílnúmer: ")
                    #Hendir manni til baka ef maður slær inn t eða h
                    if registration_num == "t" or registration_num == "h":
                        if registration_num == "h":
                            done = True
                        break
                    #Tekur inn bílnúmerið og athugar hvort það sé löglegt
                    car_found, legal_reg_num = self.__car_service.car_find(registration_num)
                    if not car_found:
                        if not legal_reg_num:
                            choice = input('1.  Reyna aftur\nt.  Tilbaka\nh.  Heim\n')
                        else:
                            #Fall sem skilar tekur inn tvö gildi og skilar villuskilaboðum
                            choice = error_handle("Bíllinn", registration_num)
                        if choice == "1":
                            print_header(prompt)
                            continue
                        elif choice == "t" or choice == "h":
                            if choice == "h":
                                done = True
                            break
                    exit_info, done = self.view_car(car_found)
            #Skrá nýjan bíl, sjá make_car fallið í CarService.
            elif action == "2":
                prompt += " / Skrá nýjan bíl"
                print_header(prompt)
                new_car = self.__car_service.make_car(prompt)
                #Fallið sem býr til nýjan bíl (sjá fallið nánar) og skilar annað hvort instance af bíl eða streng
                if type(new_car) == Car:
                    exit_info, done = self.view_car(new_car)
                #Ef fallið á undan skilar ekki streng þá er 
                else: 
                    if new_car == "h":
                        done = True
            #Skoða lausa bíla, sjá get_available_cars fallið í CarService klasanum.
            elif action == "3":
                exit_info = ""
                prompt += " / Skoða lausa bíla"
                print_header(prompt)
                while exit_info == "":
                    #Prentar út alla lausa bíla á ákveðnu tímabili og skilar True/False eftir því 
                    self.__car_service.get_available_cars(prompt)
                    choice = ""
                    while choice != "1":
                        choice = input("1.  Skoða fleiri lausa bíla\nt.  Tilbaka\nh.  Heim\n").lower()
                        if choice == "t" or choice == "h":
                            if choice == "h":
                                done = True
                            exit_info = "Tilbaka"
                            break
                        print_header(prompt)
            elif action == "4":
                exit_info = ""
                prompt += " / Skoða bíla í útleigu"
                print_header(prompt)
                while exit_info == "":
                    busy_cars_dict = self.__car_service.get_busy_cars(prompt)
                    self.__car_service.print_car_dict(busy_cars_dict)
                    choice = ""
                    while choice != "1":
                        choice = input("1.  Skoða fleiri bíla í útleigu\nt.  Tilbaka\nh.  Heim\n")
                        if choice == "t" or choice == "h":
                            if choice == "h":
                                done = True
                            exit_info = "Tilbaka"
                            break
                        print_header(prompt)
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
                

