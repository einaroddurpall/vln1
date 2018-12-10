from os import system,name
from services.StaffService import StaffService
from time import sleep
from models.ui_methods import print_header, error_handle
from models.Staff import Staff

class StaffMenu:

    def __init__(self):
        self.__staff_service = StaffService()
        self.staff_menu()

    def staff_menu(self):
        """her er hægt að skrá nýjan aðgan að forritinu"""
        done = False
        while not done:
            prompt = "Heimasíða / Aðgangs leyfi"
            print_header(prompt)
            action = input("1. Skrá nýjan Starfsmann\n2. Leita af starfsmanni\n4. Heim\n")
            if action == "1":
                prompt += " / Skrá nýjan Starfsmann"
                print_header(prompt)
                self.__staff_service.customer_register()
            elif action == "2":
                prompt += " / leita af Starfsmann"
                print_header(prompt)
            else:
                done = True
