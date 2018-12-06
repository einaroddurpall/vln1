from os import system,name
from time import sleep
from datetime import date
from services.CarService import CarService
from services.CustomerService import CustomerService
from services.OrderService import OrderService
from models.Car import Car, make_car_type
from models.Customer import Customer
from models.Car import make_car_type
from models.Order import Order
import string

def make_date(a_date):
    new_string = ""
    for letter in a_date:
        if letter in string.digits:
            new_string += letter
    day = new_string[:2]
    month = new_string[2:4]
    year = new_string[4:]
    return date(int(year), int(month), int(day))



class CarRentalUi:

    def __init__(self):
        self.__CarService = CarService()
        self.__CustomerService = CustomerService()
        self.__OrderService = OrderService()
    
    def draw_car(self):
        print("\033[1;34;1m{:<31}==============".format(""))
        sleep(0.35)
        print("{:<28}=={:<16}==".format("",""))
        sleep(0.35)
        print("{:<26}=={:<20}==".format("",""))
        sleep(0.35)
        print("{:<24}=={:<24}==".format("",""))
        sleep(0.35)
        print("{:<11}============={:<28}==============".format("",""))
        sleep(0.35)
        print("{:<10}={:<55}=".format("",""))
        sleep(0.35)
        print("{:<10}={:<56}=".format("",""))
        sleep(0.35)
        print("{:<10}=        ==={:<34}===        =".format("",""))
        sleep(0.35)
        print("{:<10}=      =     ={:<30}=     =      =".format("",""))
        sleep(0.35)
        print("{:<11}==== =       = ========================== =       = ====".format(""))
        sleep(0.35)
        print("{:<17}=     ={:<30}=     =".format("",""))
        sleep(0.35)
        print("{:<19}==={:<34}===".format("",""))
        sleep(1.5)
        print("{:<35}CarHub \033[0m".format(""))
        sleep(2)
        system('clear')

    def print_header(self, prompt=""):
        """ Hreinsar terminal og prentar út header með slóð """
        system('clear')
        print("Heimasíða", end="")
        print(prompt)
        print("="*40)

    def car_menu(self, prompt):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma bíl við """
        self.print_header(prompt)
        action = input("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu\n")
        if action == "1":
            prompt += " / Skoða bíl"
            self.print_header(prompt)
            exit_info = ''
            while exit_info == '':
                registration_num = input("Bílnúmer: ")
                car_found_info = self.__CarService.car_find(registration_num)
                system('clear')
                self.print_header(prompt)
                print(car_found_info)
                print()
                exit_info = input("Sláðu inn eitthvað til að fara heim: ")
            pass

        elif action == "2":
            prompt += " / Skrá nýjan bíl"
            self.print_header(prompt)
            new_car = Car()
            new_car = new_car.make_car()
            system('clear')
            self.print_header(prompt)
            print("Bíll skráður í kerfið")
            sleep(3)
            self.__CarService.car_register(new_car)
        elif action == "3":
            prompt += " / Skoða lausa bíla"
            self.print_header(prompt)
            valid_date = False
            while valid_date != True:
                try:
                    date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                    date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                    car_busy_dict = self.__CarService.get_busy_cars(date1, date2)
                    valid_date = True
                except: 
                    print("Vinsamlegast sláðu inn gilda dagsetningu")
            all_car_dict = self.__CarService.make_all_cars_dict()
            for key in all_car_dict:
                for car in all_car_dict[key]:
                    if car in car_busy_dict[key]:
                        all_car_dict[key].remove(car)
            if all_car_dict:
                question = input("Viltu leita af ákveðnari tegund (j/n)? ")
                if question == "j":
                    car_type = make_car_type()
                    if car_type in all_car_dict.keys():
                        print("{}:".format(car_type))
                        print("="*60)
                        for car_info in all_car_dict[car_type]:
                            print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
                        print("="*60)
                    else:
                        print("Enginn bíll laus í þessari bílategund á þessum tíma")

                else:
                    for key,val in all_car_dict.items():
                        if all_car_dict[key] == []:
                            continue
                        print(key[0].upper() + key[1:] + ":")
                        print("="*60)
                        for car_info in val:
                            print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
                        print("="*60)
            else:
                print("Enginn laus bíll á þessum tíma")
            exit_info = input("Sláðu inn eitthvað til að fara heim: ")

        elif action == "4":
            prompt += " / Skoða bíla í útleigu"
            self.print_header(prompt)
            valid_date = False
            while valid_date != True:
                try:
                    date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                    date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                    car_info_dict = self.__CarService.get_busy_cars(date1, date2)
                    valid_date = True
                except: 
                    print("Vinsamlegast sláðu inn gilda dagsetningu")
            if car_info_dict:
                question = input("Viltu leita af ákveðnari tegund (j/n)? ")
                if question == "j":
                    car_type = make_car_type()
                    if car_type in car_info_dict.keys():
                        print("{}:".format(car_type))
                        print("="*60)
                        for car_info in car_info_dict[car_type]:
                            print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
                        print("="*60)
                    else:
                        print("Enginn bíll í útleigu í þessari bílategund á þessum tíma")
                else:
                    for key,val in car_info_dict.items():
                        print("{}:".format(key))
                        print("="*60)
                        for car_info in val:
                            print("{:>10}{:>20}{:>8}{:>15}".format(car_info[0],car_info[1],car_info[2],car_info[3],))
                        print("="*60)
            else: 
                print("Enginn bíll í útleigu á þessum tíma")
            exit_info = input("Sláðu inn eitthvað til að fara heim: ")

    def customer_menu(self, prompt):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma viðskiptavinum við """
        done = False
        while not done:
            self.print_header(prompt)
            action = input("1.  Leita að viðskiptavin\n2.  Skrá nýjan viðskiptavin\n")
            if action == "1":
                prompt += " / Leita að viðskiptavin"
                self.print_header(prompt)
                ssn = input("Kennitala: ")
                customer = self.__CustomerService.check_ssn(ssn)
                system('clear')
                self.print_header(prompt)
                choice = ""
                if customer:
                    while choice is not "4":
                        print(customer)
                        choice = input("\n1.  Sjá pantanir\n2.  Breyta skráningu\n3.  Afskrá viðskiptavin\n4.  Heimasíða\n")
                        if choice == "1":
                            prompt += " / Sjá pantanir"
                            self.print_header(prompt)
                            #Vantar fall til að sjá pantanir
                        elif choice == "2":
                            prompt += " / Breyta skráningu"
                            self.print_header(prompt)
                            customer.customer_change_info()
                        elif choice == "3":
                            prompt += " / Afskrá viðskiptavin"
                            self.print_header(prompt)
                            # Vantar fall til að afskrá viðskiptavin
                else:
                    choice = input('Kennitalan: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\n2.  Heimasíða'.format(ssn))
                    if choice == "2":
                        done = True

            elif action == "2":
                prompt += " / Skrá nýjan viðskiptavin"
                self.print_header(prompt)
                self.__CustomerService.customer_register()
                done = True

    def order_menu(self, prompt):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma pöntunum við """
        self.print_header(prompt)
        action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Skila bíl\n")
        if action == "1":
            prompt += " / Skoða pöntun"
            self.print_header(prompt)
            order_num = input("Pöntunarnúmer: ")
            # self.__OrderService
        elif action == "2":
            prompt += " / Skrá nýja pöntun"
            self.print_header(prompt)
            self.__OrderService.make_order_info()
            input("Pöntun skráð.")
            
        elif action == "3":
            prompt += " / Skila bíl"
            self.print_header(prompt)
            pass

    def main_menu(self):
        """ Main menu er loop sem hættir þegar q er sett inn."""
        action = ""
        while action != "q":
            prompt = ""
            self.print_header(prompt)
            action = input("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða eða skrá pantanir\n")
            if action == "1":
                prompt = " / Bílar"
                self.car_menu(prompt)
            elif action == "2":
                prompt = " / Viðskiptavinir"
                self.customer_menu(prompt)
            elif action == "3":
                prompt = " / Skoða eða skrá pantanir"
                self.order_menu(prompt)