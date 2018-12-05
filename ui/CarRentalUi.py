from os import system,name
from time import sleep
from services.CarService import CarService
from services.CustomerService import CustomerService
from models.Car import Car
from models.Customer import Customer
from datetime import date
from models.Car import make_car_type

def make_date(a_date):
    day, month, year = a_date.split(".")
    return date(int(year), int(month), int(day))

class CarRentalUi:

    def __init__(self):
        self.__CarService = CarService()
        self.__CustomerService = CustomerService()
    
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
        system('clear')
        print("Heimasíða", end="")
        print(prompt)
        print("="*40)

    def home_menu(self, prompt):
        self.print_header(prompt)
        action = input("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða eða skrá pantanir\n")
        return action

    def car_menu(self, prompt):
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
                print(car_found_info)
                exit_info = input("Enter something to go back: ")
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
            pass

    def customer_menu(self, prompt):
        self.print_header(prompt)
        action = input("1.  Leita að viðskiptavin\n2.  Skrá nýjan viðskiptavin\n")
        if action == "1":
            pass
        elif action == "2":
            prompt += " / Skrá nýjan viðskiptavin"
            self.print_header(prompt)
            new_customer = Customer()
            new_customer = new_customer.make_customer()
            self.__CustomerService.customer_register(new_customer)

    def order_menu(self, prompt):
        self.print_header(prompt)
        action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Skila bíl\n")
        if action == "1":
            prompt += " / Skoða pöntun"
            self.print_header(prompt)
            pass
        elif action == "2":
            prompt += " / Skrá nýja pöntun"
            self.print_header(prompt)
            ssn = input("Kennitala viðskiptavinar: ")
            valid_ssn = False
            if self.__CustomerService.check_ssn(ssn):
                valid_ssn = True
            if valid_ssn:
                step1 = False
                while step1 is not True:
                    car_type = make_car_type()
                    date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                    date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                    continue_q = input("Halda áfram? (y/n) ").lower()
                    if continue_q == "y":
                        step1 = True
                    system('clear')
                step2 = False
                while step2 is not True:
                    number = input("Veldu tryggingu:\n1.  Grunntrygging\n2.  Aukatrygging\n")
                    if number == "1":
                        insurance = "basic"
                    else:
                        insurance = "extra"
                    card_info = input("Kortanúmer: ")
                    continue_q = input("Halda áfram? (y/n) ").lower()
                    if continue_q == "y":
                        step2 = True
                    system('clear')
        elif action == "3":
            prompt += " / Skila bíl"
            self.print_header(prompt)
            pass

    def main_menu(self):
        action = ""
        while action != "q":
            prompt = ""
            action = self.home_menu(prompt)
            if action == "1":
                prompt = " / Bílar"
                self.car_menu(prompt)
            elif action == "2":
                prompt = " / Viðskiptavinir"
                self.customer_menu(prompt)
            elif action == "3":
                prompt = " / Skoða eða skrá pantanir"
                self.order_menu(prompt)