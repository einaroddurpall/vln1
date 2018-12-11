from datetime import date
import datetime
from datetime import timedelta
from models.Car import Car
from models.Customer import Customer
from models.Order import Order
from models.Functions import make_date_list

class OrderRepository:

    def __init__(self):
        self.__order_list = self.get_orders()
        self.__names = self.get_names()
        

    def get_names(self):
        orders = self.__order_list
        names = []
        for order in orders:
            names.append(order.get_order_name())
        return names
    
    def get_orders(self):
        """Setur pantanir í lista"""
        order_list = []
        with open("./data/orders.csv", encoding = "UTF-8") as order_file:
            for row in order_file.readlines():
                    order_name, customer, car, date1, date2, insurance, card_info, price, complete = row.split(";")
                    date1 = eval(date1)
                    date2 = eval(date2)
                    date_list = make_date_list(date1, date2)
                    order = Order(eval(customer), eval(car), date_list, insurance, card_info, order_name, price, complete)
                    order_list.append(order)
        return order_list
    
    def add_order(self, order):
        """Bætir við pöntun í pöntunarskjalið"""
        #self.__orders += 1
        self.get_unique_name(order)
        with open("./data/orders.csv", "a", encoding = "UTF-8") as order_file:
            order_file.write(order.__repr__() + '\n')
        self.__order_list.append(order)

    def get_order_list(self):
        return self.__order_list

    def get_unique_name(self, order):
        names = self.__names
        counter = 1
        while True:
            unique_name = "Pöntun " + str(counter)
            counter += 1
            if unique_name not in names:
                order.set_order_name(unique_name)
                self.__names.append(unique_name)
                break

    def update_order_list(self):
        with open("./data/orders.csv", "w", encoding = "UTF-8") as orders_file:
            new_file = ""
            for order in self.__order_list:
                new_file += order.__repr__()
            orders_file.seek(0)
            orders_file.truncate()
            orders_file.write(new_file)
    