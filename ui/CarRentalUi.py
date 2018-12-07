from os import system, name
from time import sleep
from datetime import date
import string
from ui.CarUI import CarMenu
from ui.CustomerUI import CustomerMenu
from ui.OrderUI import OrderMenu
from models.ui_methods import print_header

class CarRentalUi:

    def __init__(self):
        self.__CarUI = CarMenu
        self.__OrderUI = OrderMenu
        self.__CustomerUI = CustomerMenu

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
        """ Main menu er loop sem hættir þegar q er sett inn."""
        action = ""
        while action != "q":
            prompt = "Heimasíða"
            print_header(prompt)
            action = input("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða eða skrá pantanir\n")
            if action == "1":
                
                self.__CarUI()
            elif action == "2":
                prompt += " / Viðskiptavinir"
                self.__CustomerUI(prompt)
            elif action == "3":
                prompt += " / Skoða eða skrá pantanir"
                self.__OrderUI(prompt)