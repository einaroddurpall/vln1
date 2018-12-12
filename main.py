from ui.CarRentalUi import CarRentalUi
from os import system

def main():
    """Prentar út hellaðan bíl og keyrir aðal UI-ið"""
    system('clear')
    ui = CarRentalUi()
    #ui.draw_car()
    ui.main_menu()

main()