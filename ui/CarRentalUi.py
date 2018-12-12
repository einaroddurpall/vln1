from os import system, name
from time import sleep
from datetime import date
import string
from ui.CarUI import CarMenu
from ui.CustomerUI import CustomerMenu
from ui.OrderUI import OrderMenu
from ui.StaffUI import StaffMenu
from models.Functions import print_header
from services.StaffService import StaffService

class CarRentalUi:

    def __init__(self):
        self.__carUI = CarMenu
        self.__orderUI = OrderMenu
        self.__customerUI = CustomerMenu
        self.__staffUI = StaffMenu
        self.__staff_service = StaffService()

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
        sleep(1)
        print("{:<35}CarHub \033[0m".format(""))


    def main_menu(self):
        """ Main menu er loop sem hættir þegar q er sett inn. Á flestum input stöðum (fyrir utan þegar beðið er um dagsetningar eða 
        bílaflokk) er hægt að setja inn "t" til að fara tilbaka eða "h" til að fara aftur á þessa síðu. """
        login = False
        while not login:
            username = input("Username: ")
            password = input("Password: ")
            login, admin = self.__staff_service.check_login(username, password)
            if login == False:
                system('clear')
                print("Innskráning mistókst.")
                sleep(1)
        action = ""
        while action != "q":
            prompt = "Heimasíða"
            print_header(prompt)
            if admin:
                action = input("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða eða skrá pantanir\n4.  Starfsmenn\nq.  Skrá út\n").lower()
                if action == '4':
                    self.__staffUI()
            else:
                action = input("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða eða skrá pantanir\nq.  Skrá út\n").lower()
            if action == "1":
                #car.car_menu()
                self.__carUI()
            elif action == "2":
                #customer.customer_menu()
                self.__customerUI()
            elif action == "3":
                #order.order_menu()
                self.__orderUI()
