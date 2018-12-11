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
from models.Functions import print_header, error_handle, pretty_str

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
            choice = new_order.change_info(str(step), self.__car_service, self.__customer_service, prompt)
            if choice == "t":
                return "t"
            elif choice == "h":
                return "h"
        continue_q = input("Er allt rétt? (j/n) ").lower()
        if continue_q != "j":
            self.change_order_info(new_order, True, prompt)
        price = calc_price(new_order)
        new_order.set_price(price)
        self.__order_repo.add_order(new_order)
        return new_order
        
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
            order.change_info(choice, self.__car_service, self.__customer_service, prompt)
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
        order_found = False
        finished_completing_orders = False
        while not finished_completing_orders:
            while not order_found:
                print_header(prompt)
                order_list = self.__order_repo.get_order_list()
                order_to_complete_list = []
                for order in order_list:
                    if order.get_order_complete() != True and order.get_last_day() == date.today():
                        order_to_complete_list.append(order)
                if order_to_complete_list == []:
                    print("Engin pöntun þarf að klára í dag.")
                    sleep(2)
                    order_found = True
                    finished_completing_orders = True
                else:
                    for order in order_to_complete_list:
                        print(order)
                        print()
                    order_to_change = input("Hvaða pöntun viltu klára? ")
                    if order_to_change == "t" or order_to_change == "h":
                        return order_to_change
                    for order in order_to_complete_list:
                        if order_to_change == order.get_order_name():
                            order_to_complete = order
                            break
                        order_to_complete = False
                    if not order_to_complete:  # ss það finnst engin pöntun með þessu nafni
                        choice = error_handle("Pöntun", order_to_change)
                        if choice == "t" or choice == "h":
                            return choice
                        print_header(prompt)
                    else:
                        car = order_to_complete.get_car()
                        order_price = int(order_to_complete.get_order_price())
                        new_milage_boolean = False
                        while not new_milage_boolean:
                            new_milage = int(input("Hvað er bíllinn núna keyrður? "))
                            milage_difference = new_milage - car.get_milage()
                            if 0 < milage_difference:
                                new_milage_boolean = True
                            else:
                                print("Villa: Bíllinn getur ekki verið minna keyrður eftir leigu.")
                        day_price = order_price // len(order_to_complete.get_date_list())
                        final_payment = int(order_price + milage_difference // 150 * 0.02 * day_price)
                        final_payment = pretty_str(final_payment, "ISK")
                        car.set_milage(new_milage)
                        self.__car_service.update_car_list(car)
                        order_to_complete.set_car(car)
                        order_to_complete.set_complete(True)
                        self.__order_repo.update_order_list()
                        print_header(prompt)
                        print("Viðskiptavinur þarf að greiða {}\nPöntun er nú kláruð".format(final_payment))
                        choice = input("1.  Velja aðra pöntun til að klára\n2.  Tilbaka\n3.  Heim\n")
                        if choice == "2" or choice == "3":
                            finished_completing_orders = True
                        else:
                            order_found = False