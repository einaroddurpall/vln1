from datetime import datetime, timedelta
from os import system
from models.Car import make_car_type
from models.Order import Order
from services.CustomerService import CustomerService
from services.CarService import CarService
from time import sleep
from datetime import date

def make_date_list(date1, date2):
    date_list = []
    date_to_list = date1
    while date1 <= date2:
        date_list.append(date_to_list)
        date_to_list += timedelta(days=1)
    return date_list

class OrderService:

    def __init__(self):
        self.__CustomerService = CustomerService()
        self.__OrderService = OrderService()
        self.__CarService = CarService()

    def make_date(self, a_date):
        day, month, year = a_date.split(".")
        return date(int(year), int(month), int(day))

    def get_order_info(self):
        ssn = input("Kennitala viðskiptavinar: ")
        valid_ssn = False
        while valid_ssn is not True:
            if self.__CustomerService.check_ssn(ssn):
                valid_ssn = True
            else:
                ssn = input("Kennitala ekki á skrá\nKennitala viðskiptavinar\n")
        step1 = False
        while step1 is not True:
            car_type = make_car_type()
            date1 = input("Afhendingardagur (DD.MM.YYYY): ")
            date2 = input("Skiladagur (DD.MM.YYYY): ")
            date_list = make_date_list(date1, date2)
            self.car = self.rent_car(car_type, date_list)
            if self.car:
                continue_q = input("Halda áfram? (y/n) ").lower()
                if continue_q == "y":
                    step1 = True
                system('clear')
            else:
                print("Enginn bíll laus með þessi skilyrði")
                sleep(2)
                system('clear')
                print("Heimasíða / Skoða eða skrá pantanir / Skrá pantanir")
                print("="*40)
        step2 = False
        while step2 is not True:
            number = input("Veldu tryggingu:\n1.  Grunntrygging\n2.  Aukatrygging\n")
            if number == "1":
                insurance = "basic"
            else:
                insurance = "extra"
            card_info = input("Kortanúmer: ")
            continue_q = input("Halda áfram? (y/n) ").lower()
            if continue_q == "y":
                step2 = True
            system('clear')
            self.rent_car(car_type, date_list)
            return Order(ssn, car_type, date_list, insurance, card_info)
        
    def rent_car(self, car_type, date_list):
        """ Þetta fall tekur á móti upplýsingum um pöntunina frá UI,
            sækir lista af viðeigandi bílaflokk og fer í gegnum dagsetningarnar
            þangað til bíll finnst sem er laus. Ef enginn finnst þá kemur
            viðeigandi skilaboð """
        if car_type.lower() == "sedan":
            car_type_list = self.__CarService.__car_repo_sedan.get_carlist()
        elif car_type.lower() == "five seat suv":
            car_type_list = self.__CarService.__car_repo_five_seat_suv.get_carlist()
        elif car_type.lower() == "minibus":
            car_type_list = self.__CarService.__car_repo_minibus.get_carlist()
        elif car_type.lower() == "seven seat suv":
            car_type_list = self.__CarService.__car_repo_seven_seat_suv.get_carlist()
        elif car_type.lower() == "small car":
            car_type_list = self.__CarService.__car_repo_small_car.get_carlist()

        date_repo = self.__CarService.get_date_repo()
        date_dict = date_repo.get_date_dict()
        for car in car_type_list:
            is_rentable = True
            for date in date_list:
                if date in date_dict:
                    if car in date_dict[date]:
                        is_rentable = False
                        break
            if is_rentable:
                return car
        return None