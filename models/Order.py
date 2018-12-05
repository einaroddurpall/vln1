from os import system
from models.Car import make_car_type
from services.CustomerService import CustomerService
from services.OrderService import OrderService
from services.CarService import CarService
from datetime import date

class Order:

    def __init__(self, ssn="", car_type="", date_list=[], insurance="", card_info=""):
        self.__CustomerService = CustomerService()
        self.__OrderService = OrderService()
        self.__CarService = CarService()
        self.__ssn = ssn
        self.__car_type = car_type
        self.__date_list = date_list
        self.__insurance = insurance
        self.__card_info = card_info