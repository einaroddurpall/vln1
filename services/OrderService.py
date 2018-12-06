from datetime import datetime, timedelta
from os import system
from models.Car import make_car_type
from models.Order import Order
from services.CustomerService import CustomerService
from services.CarService import CarService
from time import sleep
from datetime import date
from repositories.OrderRepository import OrderRepsitory

def make_date(a_date):
    day, month, year = a_date.split(".")
    return date(int(year), int(month), int(day))

def make_date_list(date1, date2):
    date_list = []
    date_to_list = date1
    while date_to_list <= date2:
        date_list.append(date_to_list)
        date_to_list += timedelta(days=1)
    return date_list

class OrderService:

    def __init__(self):
        self.__OrderRepo = OrderRepsitory()
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()
        self.car = None

    def make_date(self, a_date):
        day, month, year = a_date.split(".")
        return date(int(year), int(month), int(day))

    def make_order_info(self):
        ssn = input("Kennitala viðskiptavinar: ")
        valid_ssn = False
        while valid_ssn is not True:
            customer = self.__CustomerService.check_ssn(ssn)
            if customer:
                valid_ssn = True
            else:
                ssn = input("Kennitala ekki á skrá\nKennitala viðskiptavinar\n")
        step1 = False
        while step1 is not True:
            car_type = make_car_type()
            date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
            date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
            date_list = make_date_list(date1, date2)
            car = self.rent_car(car_type, date_list)
            if car:
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
                insurance = "skyldu trygging"
            else:
                insurance = "aukaleg trygging"
            card_info = input("Kortanúmer: ")
            continue_q = input("Halda áfram? (y/n) ").lower()
            if continue_q == "y":
                step2 = True
            system('clear')
            new_order = Order(customer, car, date_list, insurance, card_info)
            self.__OrderRepo.add_order(new_order)

    def rent_car(self, car_type, date_list):
        """ Þetta fall tekur á móti car_type og date_list, býr til carlist fyrir viðeigandi car_type og athugar hvort einhver
            bíll í þessum carlist sé laus á dögunum í date_list """
        if car_type.lower() == "sedan":
            car_type_list = self.__CarService._car_repo_sedan.get_carlist()
        elif car_type.lower() == "five seat suv":
            car_type_list = self.__CarService._car_repo_five_seat_suv.get_carlist()
        elif car_type.lower() == "minibus":
            car_type_list = self.__CarService._car_repo_minibus.get_carlist()
        elif car_type.lower() == "seven seat suv":
            car_type_list = self.__CarService._car_repo_seven_seat_suv.get_carlist()
        elif car_type.lower() == "small car":
            car_type_list = self.__CarService._car_repo_small_car.get_carlist()

        date_repo = self.__CarService.get_date_repo()
        date_dict = date_repo.get_date_dict()
        for car in car_type_list:
            if car.check_availability(date_list, date_dict, car_type_list):
                return car
        return None

    def get_order(self, order_num):
        pass