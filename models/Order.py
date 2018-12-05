from os import system
from models.Car import make_car_type
from services.CustomerService import CustomerService
from services.OrderService import OrderService
from datetime import date

def make_date(a_date):
    day, month, year = a_date.split(".")
    return date(int(year), int(month), int(day))



class Order:

    def __init__(self, ssn="", car_type="", date_list=[], insurance="", card_info=""):
        self.__CustomerService = CustomerService()
        self.__OrderService = OrderService()

    def get_order_info(self):
        ssn = input("Kennitala viðskiptavinar: ")
        valid_ssn = False
        if self.__CustomerService.check_ssn(ssn):
            valid_ssn = True
        if valid_ssn:
            step1 = False
            while step1 is not True:
                car_type = make_car_type()
                date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                date_list = self.__OrderService.date_list(date1, date2)
                continue_q = input("Halda áfram? (y/n) ").lower()
                if continue_q == "y":
                    step1 = True
                system('clear')
            step2 = False
            while step2 is not True:
                number = input("Veldu tryggingu:\n1.  Grunntrygging\n2.  Aukatrygging\n")
                if number == "1":
                    insurance = "basic"
                else:
                    insurance = "extra"
                card_info = input("Kortanúmer: ")
                continue_q = input("Halda áfram? (y/n) ").lower()
                if continue_q == "y":
                    step2 = True
                system('clear')
                return Order(ssn, car_type, date_list, insurance, card_info)
        else:
            system('clear')
            print("Kennitala ekki á skrá.")
            sleep(2)
            self.order_menu("Heimasíða / Skoða eða skrá pantanir")

        self.__CarService(car_type, date1, date2, insurance, card_info)

    def get_order_info(self):
        ssn = input("Kennitala viðskiptavinar: ")
        valid_ssn = False
        if CustomerService.check_ssn(self, ssn):
            valid_ssn = True
        if valid_ssn:
            step1 = False
            while step1 is not True:
                car_type = make_car_type()
                date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                continue_q = input("Halda áfram? (y/n) ").lower()
                if continue_q == "y":
                    step1 = True
                system('clear')
            step2 = False
            while step2 is not True:
                number = input("Veldu tryggingu:\n1.  Grunntrygging\n2.  Aukatrygging\n")
                if number == "1":
                    insurance = "basic"
                else:
                    insurance = "extra"
                card_info = input("Kortanúmer: ")
                continue_q = input("Halda áfram? (y/n) ").lower()
                if continue_q == "y":
                    step2 = True
                system('clear')
                return Order(ssn, car_type, datelist)
        else:
            system('clear')
            print("Kennitala ekki á skrá.")
            sleep(2)
            self.order_menu("Heimasíða / Skoða eða skrá pantanir")




#     def rent_car(self, car_type, date1, date2, insurance, card_info):
#         """ Þetta fall tekur á móti upplýsingum um pöntunina frá UI,
#             sækir lista af viðeigandi bílaflokk og fer í gegnum dagsetningarnar
#             þangað til bíll finnst sem er laus. Ef enginn finnst þá kemur
#             viðeigandi skilaboð """
#         if car_type.lower() == "sedan":
#             car_type_list = self.__car_repo_sedan.get_carlist()
#         elif car_type.lower() == "five seat suv":
#             car_type_list = self.__car_repo_five_seat_suv.get_carlist()
#         elif car_type.lower() == "minibus":
#             car_type_list = self.__car_repo_minibus.get_carlist()
#         elif car_type.lower() == "seven seat suv":
#             car_type_list = self.__car_repo_seven_seat_suv.get_carlist()
#         elif car_type.lower() == "small car":
#             car_type_list = self.__car_repo_small_car.get_carlist()
#         available_car = self.__customer_service.get_available_car(car_type_list, date1, date2)
        



#     # def get_available_car(carlist, date1, date2):
#     #     # for car in carlist