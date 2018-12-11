from datetime import datetime, timedelta
from os import system
from models.Order import Order
from time import sleep
from datetime import date
import string
from repositories.OrderRepository import OrderRepository
from repositories.CarRepository import CarRepository
from services.CarService import CarService, get_car_price
from services.CustomerService import CustomerService
from services.ChangeService import ChangeService
from models.Car import Car
from models.Functions import print_header, error_handle

def calc_price(order):
    """Calculates the price of an order"""
    car = order.get_car()
    car_type = car.get_car_type()
    base_price = get_car_price(car_type)
    dates = len(order.get_date_list())
    insurance = order.get_insurance()
    if insurance == 'Grunntrygging':
        insurance_price = 2000
    else:
        insurance_price = 3500
    return dates*(base_price + insurance_price)

class OrderService:

    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__order_list = self.__order_repo.get_order_list()
        self.__car_service = CarService()
        self.__customer_service = CustomerService()
        self.__car = None
        self.__change_service = ChangeService()
        #self.__order_num = 1

    def make_date(self, a_date):
        day, month, year = a_date.split(".")
        return date(int(year), int(month), int(day))

    def make_order_info(self, prompt):
        new_order = Order()
        for step in range(1, 5):
            choice = new_order.change_info(str(step), self.__car_service, self.__customer_service)
            if choice == "Tilbaka":
                return "Tilbaka", new_order
            elif choice == "Heim":
                return "Heim", new_order
        continue_q = input("Er allt rétt? (j/n) ").lower()
        if continue_q != "j":
            self.change_order_info(new_order, True, prompt)
        else:
            price = calc_price(new_order)
            new_order.make_price(price)
            self.__order_repo.add_order(new_order)
        return "", new_order
        
    def change_order_info(self, order, new_or_not, prompt):
        correct = False
        while not correct:
            print_header(prompt)
            print("Hverju villtu breyta:\n1. Kennitölu á pöntun\n2. Bíl og dagsetningu\n3. Tryggingu\n4. Kortanúmeri\n5. Klára Skráningu")
            legal_choice = False
            while not legal_choice:
                choice = input()
                try:
                    if int(choice) in range(1,6):
                        legal_choice = True
                    else:
                        print("Ekki valmöguleiki, veldu aftur")
                except:
                    print("Ekki valmöguleiki, veldu aftur")
            if choice == "5":
                correct = True
            order.change_info(choice, self.__car_service, self.__customer_service)
        if new_or_not:
            self.__order_repo.add_order(order)
        else:
            self.__order_repo.update_order_list()

    def get_order_by_name(self, name):
        for order in self.__order_repo.get_order_list():
            if order.get_order_name() == name:
                return order
        return None

    def get_order_by_ssn(self, ssn):
        customer = self.__customer_service.check_ssn(ssn)
        orders = []
        for order in self.__order_repo.get_order_list():
            if order.get_customer() == customer:
                orders.append(order)
        return orders
        
    def order_delete(self, order):
        self.__order_list.remove(order)
        self.__order_repo.update_order_list()

    def complete_orders(self, prompt):
        order_list = self.__order_repo.get_order_list()
        order_to_complete_list = []
        for order in order_list:
            if order.get_order_complete() != "True\n":
                if order.get_last_day() == date.today():
                    order_to_complete_list.append(order)
        # order_found = False
        # while not order_found:
        for order in order_to_complete_list:
            print(order)
        choice = input("Hvaða pöntun viltu klára? ")
        for order in order_to_complete_list:
            if choice == order.get_order_name():
                order_to_complete = order
                break
        new_milage = int(input("Hvað er bíllinn núna keyrður? "))  # Villucheck hvort bíll sé nokkuð minna keyrður en hann var
        milage_difference = new_milage - order_to_complete.get_car().get_milage()
        day_price = int(order_to_complete.get_order_price()) // len(order_to_complete.get_date_list())
        final_payment = int(order_to_complete.get_order_price()) + milage_difference // 150 * 0.02 * day_price
        car = order_to_complete.get_car()
        car.set_milage(new_milage)
        self.__car_service.update_car_list(car)
        order_to_complete.set_car(car)
        order_to_complete.set_complete(True)
        self.__order_repo.update_order_list()
        print_header(prompt)
        print("Viðskiptavinur þarf að greiða {} kr.\nPöntun er nú kláruð".format(int(final_payment)))
        input()
