from os import system,name
from time import sleep
from datetime import date
from services.CarService import CarService
from services.CustomerService import CustomerService
from services.OrderService import OrderService
from models.Car import Car
from models.Customer import Customer
from models.Car import make_car_type
from models.Order import Order

def make_date(a_date):
    day, month, year = a_date.split(".")
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
            self.__CarService.car_register(new_car)
        elif action == "3":
            prompt += " / Skoða lausa bíla"
            pass
        elif action == "4":
            prompt += " / Skoða bíla í útleigu"
            self.print_header(prompt)
            date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
            date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
            car_info = self.__CarService.get_busy_cars(date1, date2)
            question = input("Viltu leita af ákveðnari tegund (y/n)? ")
            if question == "y":
                car_type = input("Sláðu inn tegunds bíl :")
                for car in car_info:
                    if car.get_car_type() != car_type:
                        car_info.remove(car)
                print(car_type + ":")
            for car in car_info:
                print("-"*30)
                print("{}, {}, {}, {}".format(car.get_sub_type(), car.get_registration_num(), car.get_milage(), car.get_transmission()))
            print()
            exit_info = input("Sláðu inn eitthvað til að fara heim: ")


    def customer_menu(self, prompt):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma viðskiptavinum við """
        self.print_header(prompt)
        action = input("1.  Leita að viðskiptavin\n2.  Skrá nýjan viðskiptavin\n")
        if action == "1":
            prompt += " / Leita að viðskiptavin"
            self.print_header(prompt)
            ssn = input("Sláðu inn kennitölu: ")
            customer_info = self.__CustomerService.check_ssn(ssn)
            system('clear')
            self.print_header(prompt)
            print(customer_info)
            exit_info = ''
            print()
            while exit_info == '':
                exit_info = input("Sláðu einn eitthvað til að fara heim: ")

        elif action == "2":
            prompt += " / Skrá nýjan viðskiptavin"
            self.print_header(prompt)
            new_customer = Customer()
            new_customer = new_customer.make_customer()
            self.__CustomerService.customer_register(new_customer)

    def order_menu(self, prompt):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma pöntunum við """
        self.print_header(prompt)
        action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Skila bíl\n")
        if action == "1":
            prompt += " / Skoða pöntun"
            self.print_header(prompt)
            pass
        elif action == "2":
            prompt += " / Skrá nýja pöntun"
            self.print_header(prompt)
            new_order = self.__OrderService.get_order_info()
            if new_order:
                input("Pöntun skráð.")
            else:
                input("Enginn bíll með þessi skilyrði fannst.")
            pass
            
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