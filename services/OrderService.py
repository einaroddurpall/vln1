from datetime import datetime, timedelta
from os import system
from models.Car import make_car_type
from models.Order import Order
from services.CustomerService import CustomerService
from services.CarService import CarService
from time import sleep
from datetime import date
from repositories.OrderRepository import OrderRepository
import string

def make_date(a_date):
    new_string = ""
    for letter in a_date:
        if letter in string.digits:
            new_string += letter
    day = new_string[:2]
    month = new_string[2:4]
    year = new_string[4:]
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
        self.__OrderRepo = OrderRepository()
        self.__CustomerService = CustomerService()
        self.__CarService = CarService()
        self.__car = None
        #self.__order_num = 1

    def make_date(self, a_date):
        day, month, year = a_date.split(".")
        return date(int(year), int(month), int(day))

    def make_order_info(self):
        valid_ssn = False
        while valid_ssn is not True:
            ssn = input("Kennitala viðskiptavinar: ")
            customer = self.__CustomerService.check_ssn(ssn)
            if customer:
                valid_ssn = True
            else:
                print("Kennitala ekki á skrá")
        step1 = False
        while step1 is not True:
            car_type = make_car_type()
            valid_date = False
            while valid_date != True:
                try:
                    date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                    date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                    date_list = make_date_list(date1, date2)
                    valid_date = True
                except: 
                    print("Vinsamlegast sláðu inn gilda dagsetningu")
                    
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
            new_order = Order(customer, car, date_list, insurance, card_info) #"Order " + str(self.__order_num))
            #self.__order_num += 1
            self.__OrderRepo.add_order(new_order)

    def rent_car(self, car_type, date_list):
        """ Þetta fall tekur á móti car_type og date_list, býr til carlist fyrir viðeigandi car_type og athugar hvort einhver
            bíll í þessum carlist sé laus á dögunum í date_list """
        if car_type.lower() == "fólksbíll":
            car_type_list = self.__CarService._car_repo_sedan.get_carlist()
        elif car_type.lower() == "fimm sæta jeppi":
            car_type_list = self.__CarService._car_repo_five_seat_suv.get_carlist()
        elif car_type.lower() == "smárúta":
            car_type_list = self.__CarService._car_repo_minibus.get_carlist()
        elif car_type.lower() == "sjö sæta jeppi":
            car_type_list = self.__CarService._car_repo_seven_seat_suv.get_carlist()
        elif car_type.lower() == "smábíll":
            car_type_list = self.__CarService._car_repo_small_car.get_carlist()

        date_repo = self.__CarService.get_date_repo()
        date_dict = date_repo.get_date_dict()
        for car in car_type_list:
            if car.check_availability(date_list, date_dict, car_type_list):
                return car
        return None

    def get_order(self, order_num):
        pass