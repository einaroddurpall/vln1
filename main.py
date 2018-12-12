from ui.CarRentalUi import CarRentalUi
from os import system

def main():
    system('clear')
    ui = CarRentalUi()
    #ui.draw_car()
    ui.main_menu()

main()