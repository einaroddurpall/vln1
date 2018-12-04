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
    registration_num = input("Enter registration number: ")
    car_type = input("Enter car type: ")
    sub_type = input("Enter sub type: ")
    transmission = input("Enter the transmission: ")
    milage = input("Enter the milage: ")
    is_rentable = True
    history = ""
    new_car = Car(registration_num, car_type, sub_type, transmission, milage, is_rentable, history)
    return new_car

class CarRentalUi:

    def __init__(self):
        self.__CarService = CarService()

    def main_menu(self):
        action = ""
        prompt = ""
        while action != "q":
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
                    break
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