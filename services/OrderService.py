from datetime import datetime, timedelta
from os import system
from models.Order import Order
from services.CarService import CarService
from time import sleep
from datetime import date
from repositories.OrderRepository import OrderRepository
import string
from services.CustomerService import CustomerService
from services.ChangeService import ChangeService

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

    def make_order_info(self):
        new_order = Order()
        for step in range(1, 5):
            choice = new_order.change_info(str(step), self.__car_service, self.__customer_service)
            if choice == "Tilbaka":
                return "Tilbaka"
            elif choice == "Heim":
                return "Heim"
        continue_q = input("Er allt rétt? (j/n): ").lower()
        if continue_q != "j":
            self.change_order_info(new_order, True)
        else:
            self.__order_repo.add_order(new_order)

        
    def change_order_info(self, order, new_or_not):
        correct = False
        while not correct:
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
