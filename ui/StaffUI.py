from os import system,name
from services.StaffService import StaffService
from time import sleep
from models.ui_methods import print_header, error_handle

class StaffMenu:

    def __init__(self):
        self.__staff_service = StaffService()
        self.staff_menu()

    def staff_menu(self):
        """her er hægt að skrá nýjan aðgan að forritinu"""
        done = False
        while not done:
            prompt = "Heimasíða / Skrá nýjan aðgang"
            print_header(prompt)