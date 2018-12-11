from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository
from repositories.CarRepository import CarRepository
from models.Order import Order

class ChangeService:

    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__customer_repo = CustomerRepository()
        #self.__car_repo = CarRepository()
        self.__order_list = self.__order_repo.get_order_list()
        self.__customers_list = self.__customer_repo.get_customers_list()
        #self.__cars_list = self.__car_service.get_carlist()

    def change_customer_info_consequences(self, old_customer, new_customer):
        for order in self.__order_list:
            if order.get_customer() == old_customer:
                order.set_customer(new_customer)
        self.__order_repo.update_order_list()

    def change_car_info_consequences(self, old_car, new_car):
        for order in self.__order_list:
            if order.get_car() == old_car:
                order.set_car(new_car)
        self.__order_repo.update_order_list()
