from os import system,name
from time import sleep
# from services.CarService import CarService
from models.Car import Car

def print_header():
    pass

class CarRentalUi:

    def __init__(self):
        # self.CarService = CarService()
        pass

    def main_menu(self):
        action = ""
        while action != "q":
            system('clear')
            print("Heimasíða")
            print("="*40)
            print("1.\tBílar\n2.\tViðskiptavinir\n3.\tSkoða/skrá pantanir")
            action = input().lower()




def main():
    # print("Hallo")

    # sleep(5)

    # system('clear')
    pass

main()