from datetime import date
from datetime import timedelta
from models.Car import Car
from models.Customer import Customer
from models.Order import Order
from repositories.DateRepository import DateRepository

class OrderRepository:

    def __init__(self):
        self.__order_list = self.get_orders()
        self.__date_repo = DateRepository()
    
    def get_orders(self):
        """Setur pantanir í lista"""
        order_list = []
        with open("./data/orders.csv", encoding = "UTF-8") as order_file:
            for row in order_file:
                order = eval(row.strip)
                order_list.append(order)
        return order_list
    
    def add_order(self, order):
        """Bætir við pöntun í pöntunarskjalið og setur bíl í DateRepository fyrir tímabilið"""
        with open("./data/orders.csv", "a", encoding = "UTF-8") as order_file:
            order_file.write(order.__repr__() + '\n')
        self.__order_list.append(order)
        for date in order.get_date_list():
            self.__date_repo.add_car_to_date(date, order.get_car())

    def get_order_list(self):
        return self.__order_list
    

# def make_date_list(date1, date2):
#     date_list = []
#     date_to_list = date1
#     while date_to_list <= date2:
#         date_list.append(date_to_list)
#         date_to_list += timedelta(days=1)
#     return date_list

#order_repo = OrderRepository()
# customer  =Customer('Einar Oddur Páll Rúnarsson','2505983519','aaa@gmail.is','8222222','1111111111111111','Þessi viðskiptavinur hefur aldrei tekið bíl á leigu.')
# a_car = Car('AK-555','Smárúta','RISA bIll','Sjálfskiptur',60000,True,'This car has no history of rental.')
# date_list = make_date_list(date(2018,12,5), date(2018,12,8))
# insurance = "aukatrygging"
# an_order = Order(customer, a_car, date_list, insurance)
# order_repo.add_order(an_order)