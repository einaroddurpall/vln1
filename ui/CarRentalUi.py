from os import system,name
from time import sleep
from services.CarService import CarService
from models.Car import Car

def print_header(prompt=""):
    system('clear')
    print("Heimasíða", end="")
    print(prompt)
    print("="*40)

def get_action():
    return input()

def home_menu(prompt):
    print_header(prompt)
    print("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða/skrá pantanir")
    return get_action()

def car_menu(prompt):
    print_header(prompt)
    print("1.  Skoða bíl\n2.  Skrá nýjan bíl\n3.  Skoða lausa bíla\n4.  Skoða bíla í útleigu")
    return get_action()

def make_car(prompt):
    print_header(prompt)
    registration_num = input("Bílnúmer: ")
    valid_car_type = False
    while valid_car_type is False:
        print("Flokkur bíls:")
        car_type = input("1.  Fólksbíll\n2.  Smábíll\n3.  Fimm sæta jeppi\n4.  Sjö sæta jeppi\n5.  Smárúta\n")
        if car_type == "1":
            car_type = "sedan"
        elif car_type == "2":
            car_type = "small car"
        elif car_type == "3":
            car_type = "five seat suv"
        elif car_type == "4":
            car_type = "seven seat suv"
        elif car_type == "5":
            car_type = "minibus"
        else:
            continue
        valid_car_type = True
    sub_type = input("Tegund bíls: ")
    transmission = input("1.  Sjálfskiptur\n2.  Beinskiptur\n")
    valid_transmission = False
    while valid_transmission is False:
        if transmission == "1":
            transmission = "Sjálfskiptur"
        elif transmission == "2":
            transmission = "Beinskiptur"
        else:
            continue
        valid_transmission = True
    milage = input("Akstur: ")
    is_rentable = True
    history = ""
    new_car = Car(registration_num, car_type, sub_type, transmission, milage, is_rentable, history)
    return new_car

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
        

    def main_menu(self):
        action = ""
        while action != "q":
            prompt = ""
            action = home_menu(prompt)
            if action == "1":
                prompt = " / Bílar"
                action = car_menu(prompt)
                if action == "1":
                    prompt += " / Skoða bíl"
                    pass
                elif action == "2":
                    prompt += " / Skrá nýjan bíl"
                    new_car = make_car(prompt)
                    self.__CarService.car_register(new_car)
                    print("Sucess")
                elif action == "3":
                    prompt += " / Skoða lausa bíla"
                    pass
                elif action == "4":
                    prompt += " / Skoða bíla í útleigu"
                    pass




# def main():
#     # print("Hallo")

#     # sleep(5)

#     # system('clear')
#     ui = CarRentalUi()
#     ui.main_menu()

# main()