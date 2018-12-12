from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository
from repositories.CarRepository import CarRepository
from repositories.PriceRepository import PriceRepository
from models.Order import Order
from models.Car import Car

class ChangeService:

    def __init__(self):
        """Þessi klasi sér um að koma breytingum milli service klasa. Ef upplýsingum
        er breytt um bíl eða viðskiptavin þá uppfærast viðeigandi pantanir."""
        self.__order_repo = OrderRepository()
        self.__customer_repo = CustomerRepository()
        self.__order_list = self.__order_repo.get_order_list()
        self.__customers_list = self.__customer_repo.get_customers_list()

    def change_customer_info_consequences(self, old_customer, new_customer):
        """Tekur við viðskiptavin eins og hann var fyrir breytingar og eftir breytingar.
        Finnur allar pantanir þar sem óbreytti viðskiptavinurinn kemur fyrir og setur þann nýja
        í staðinn, gerist þó aðeins ef pöntuninni er ekki lokið."""
        for order in self.__order_list:
            if order.get_order_complete() == False:
                if order.get_customer() == old_customer:
                    order.set_customer(new_customer)
        self.__order_repo.update_order_list()

    def delete_customer_consequences(self, customer):
        """Tekur við viðskiptavin sem var afskráður og eyðir öllum þeim pöntunum sem voru óloknar og
        skráðar á þann viðskiptavin úr kerfinu."""
        orders_to_delete = []
        for order in self.__order_list:
            if order.get_order_complete() == False:
                if order.get_customer() == customer:
                    orders_to_delete.append(order)
        for order in orders_to_delete:
            self.__order_list.remove(order)
        self.__order_repo.update_order_list()
        input('Óloknum pöntunum viðskiptavinarins hefur verið eytt, ýttu á "Enter" til að halda áfram.')
                    
    def change_car_info_consequences(self, old_car, new_car):
        """Tekur við bíl eins og hann var fyrir breytingar og eftir breytingar. Finnur allar pantanir
        þar sem óbreytti bíllinn kemur fyrir og setur þann nýja í staðinn, gerist þó aðeins ef pöntuninni
        er ekki lokið."""
        for order in self.__order_list:
            if order.get_order_complete() == False:
                if order.get_car() == old_car:
                        order.set_car(new_car)
        self.__order_repo.update_order_list()

    def delete_car_consequences(self, car, car_service, customer_service):
        """Tekur við bíl sem var afskráður, car_service fyrir þann bíl og customer_service.
        Bílnum sem var afskráður er eytt úr öllum pöntunum sem hann kemur fyrir í og annar bíll
        úr sama flokki er settur inn í pöntunana í stað þess sem var afskráður. Ef enginn bíll
        úr sama flokki er laus fyrir tímabil pöntunarinnar er notanda boðið upp á að velja annan flokk
        þar til laus bíll finnst, sá bíll er síðan skráður inn í pöntunina."""
        car_type = car.get_car_type()
        for order in self.__order_list:
            if order.get_order_complete() == False:
                if order.get_car() == car:
                    datelist = order.get_date_list()
                    new_car = order.rent_car(car_type, datelist, car_service)
                    if type(new_car) != Car:
                        print("Bíll var skráður í pöntun/pantanir. Enginn sambærilegur bíll er laus yfir viðeigandi tímabil. Vinsamlegast skráið bíl fyrir eftirfarandi pöntun.")
                        print(order)
                        print()
                        print("Veldu flokk:")
                        order.change_info("2",car_service, customer_service, price_repo=PriceRepository())
                    else:
                        order.set_car(new_car)
        self.__order_repo.update_order_list()
