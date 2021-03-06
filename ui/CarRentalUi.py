from os import system, name
from time import sleep
from datetime import date
import string
from services.StaffService import StaffService
from models.Functions import print_header
from ui.CarUI import CarUI
from ui.CustomerUI import CustomerUI
from ui.OrderUI import OrderUI
from ui.StaffUI import StaffUI

class CarRentalUi:

    def __init__(self):
        self.__staffUI = StaffUI
        self.__staff_service = StaffService()

    def draw_car(self):
        """Teiknar bíl"""
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
        sleep(2)

    def main_menu(self):
        """ Main menu er loop sem hættir þegar q er sett inn. Á flestum input stöðum (fyrir utan þegar beðið er um dagsetningar eða 
        bílaflokk) er hægt að setja inn "t" til að fara tilbaka eða "h" til að fara aftur á þessa síðu. """
        action = ''
        while action != "q":
            system("clear")
            login = False
            while not login:
                username = input("Notandanafn: ")
                password = input("Lykilorð: ")
                #Athugar hvort notandi sé til og skilar því, notandanum og hvort hann sé admin
                login, admin, self.__staff = self.__staff_service.check_login(username, password)
                if login == False:
                    system('clear')
                    print("Innskráning mistókst.")
            action = ""
            while action != "s" and action != "q":
                prompt = "Heimasíða ('t' til að fara til baka, 'h' til að fara heim)"
                print_header(prompt)
                prompt = "Heimasíða"
                if admin:
                    action = input("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða eða skrá pantanir\n4.  Starfsmenn\ns.  Skrá út\nq.  Loka kerfi\n").lower()
                    if action == '4':
                        self.__staffUI(self.__staff)
                else:
                    action = input("1.  Bílar\n2.  Viðskiptavinir\n3.  Skoða eða skrá pantanir\ns.  Skrá út\nq.  Loka kerfi\n").lower()
                if action == "1":
                    self.__carUI = CarUI()
                    self.__carUI.car_menu()
                elif action == "2":
                    self.__customerUI = CustomerUI()
                    self.__customerUI.customer_menu()
                elif action == "3":
                    self.__orderUI = OrderUI()
                    self.__orderUI.order_menu()
