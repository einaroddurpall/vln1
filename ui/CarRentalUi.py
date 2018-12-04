from os import system,name
from time import sleep
from services.CarService import CarService
from models.Car import Car

class CarRentalUi:

    def __init__(self):
        self.__CarService = CarService()
    
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

    def get_action(self):
        return input()

    def home_menu(self, prompt):
        self.print_header(prompt)
        print("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða/skrá pantanir")
        return self.get_action()

    def car_menu(self, prompt):
        self.print_header(prompt)
        print("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu")
        action = self.get_action()
        if action == "1":
            prompt += " / Skoða bíl"
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

    # def make_car(self, prompt):
    #     self.print_header(prompt)
    #     new_car = car.make_car()

    def customer_menu(self, prompt):
        self.print_header(prompt)
        print("1.  Leita að viðskiptavin\n2.  Skrá nýjan viðskiptavin")

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




# def main():
#     # print("Hallo")

#     # sleep(5)

#     # system('clear')
#     ui = CarRentalUi()
#     ui.main_menu()

# main()