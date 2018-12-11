from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository
from repositories.CarRepository import CarRepository
from models.Order import Order
from models.Car import Car

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
            if order.get_order_complete == False:
                if order.get_customer() == old_customer:
                    order.set_customer(new_customer)
        self.__order_repo.update_order_list()

    def change_car_info_consequences(self, old_car, new_car):
            for order in self.__order_list:
                if order.get_order_complete == False:
                    if order.get_car() == old_car:
                            order.set_car(new_car)
            self.__order_repo.update_order_list()

    def delete_car_consequences(self, car, car_service, customer_service):
        car_type = car.get_car_type()
        for order in self.__order_list:
            if order.get_order_complete == False:
                if order.get_car() == car:
                    datelist = order.get_date_list()
                    new_car = order.rent_car(car_type, datelist, car_service)
                    if new_car == None:
                        print("Bíll var skráður í pöntun/pantanir. Enginn sambærilegur bíll er laus yfir viðeigandi tímabil. Vinsamlegast skráið bíl fyrir eftirfarandi pöntun.")
                        print(order)
                        order.change_info("2",car_service, customer_service)
                    else:
                        order.set_car(new_car)
        self.__order_repo.update_order_list()
