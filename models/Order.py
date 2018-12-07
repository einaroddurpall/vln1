from models.Car import make_car_type
import string
from datetime import datetime, timedelta, date
from os import system
from time import sleep
from models.Customer import make_number

class Order:
    def __init__(self, customer="", car="", date_list=[], insurance="", card_info="", order_name=""):
        self.__customer = customer
        self.__car = car
        self.__date_list = date_list
        self.__insurance = insurance
        self.__card_info = card_info
        self.__order_name = order_name
    
    def get_customer(self):
        return self.__customer

    def get_first_day(self):
        return self.__date_list[0]

    def get_last_day(self):
        return self.__date_list[-1]

    def get_car(self):
        return self.__car

    def get_date_list(self):
        return self.__date_list

    def get_insurance(self):
        return self.__insurance

    def get_card_info(self):
        return self.__card_info

    def get_order_name(self):
        return self.__order_name

    def set_order_name(self, name):
        self.__order_name = name

    def __eq__(self, other):
        return self.get_order_name() == other.get_order_name()

    def __repr__(self):
        return "{};{};{};{};{};{};{}".format(
            str(self.get_order_name()),repr(self.get_customer()), repr(self.get_car()), repr(self.get_first_day()), repr(self.get_last_day()), self.get_insurance(), self.get_card_info()
        )
    
    def __str__(self):
        return "{}\nViðskiptavinur: {}\nBíll: {}\nAfendingardagur: {}\nSkiladagur: {}\nTrygging: {}\nKortanúmer: {}".format(
            self.__order_name, self.__customer.get_name(), self.__car.get_registration_num(), str(self.get_first_day()), str(self.get_last_day()), self.__insurance, self.__card_info
        )
    
    def change_info(self, step, car_service, customer_service):
        if step == "1":
            valid_ssn = False
            while valid_ssn is not True:
                ssn = input("Kennitala viðskiptavinar: ")
                self.__customer = customer_service.check_ssn(ssn)
                if self.__customer:
                    valid_ssn = True
                else:
                    choice = input("Kennitalan {} fannst ekki.\n1.  Reyna aftur\n2.  Tilbaka\n3.  Heim\n".format(ssn))
                    if choice == "2":
                        return "Tilbaka"
                    elif choice == "3":
                        return "Heim"

        elif step == "2":
            step2 = False
            while step2 is not True:
                car_type = make_car_type()
                if car_type: 
                    valid_date = False
                    while valid_date != True:
                        try:
                            date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                            date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                            self.__date_list = make_date_list(date1, date2)
                            valid_date = True
                        except: 
                            print("Vinsamlegast sláðu inn gilda dagsetningu")
                            
                    self.__car = self.rent_car(car_type, self.__date_list, car_service)
                    if self.__car:
                        step2 = True
                        system('clear')
                    else:
                        print("Enginn bíll laus með þessi skilyrði")
                        sleep(2)
                        system('clear')
                        print("Heimasíða / Skoða eða skrá pantanir / Skrá pantanir")
                        print("="*40)
                else:
                    pass
                    # villu fall
        elif step == "3":
            step3 = False
            while step3 is not True:
                number = input("Veldu tryggingu:\n1.  Grunntrygging\n2.  Aukatrygging\n")
                if number == "2":
                    self.__insurance = "aukaleg trygging"
                    step3 = True
                else:
                    self.__insurance = "skyldu trygging"
                    step3 = True
        elif step == "4":
            self.__card_info = make_number(16, "Kortanúmer: ", "Ólöglegt kortanúmer, reyndu aftur.")
                #"Order " + str(self.__order_num))
                #self.__order_num += 1


    def rent_car(self, car_type, date_list, car_service):
        """ Þetta fall tekur á móti car_type og date_list, býr til carlist fyrir viðeigandi car_type og athugar hvort einhver
            bíll í þessum carlist sé laus á dögunum í date_list """
        if car_type.lower() == "fólksbíll":
            car_type_list = car_service._car_repo_sedan.get_carlist()
        elif car_type.lower() == "fimm sæta jeppi":
            car_type_list = car_service._car_repo_five_seat_suv.get_carlist()
        elif car_type.lower() == "smárúta":
            car_type_list = car_service._car_repo_minibus.get_carlist()
        elif car_type.lower() == "sjö sæta jeppi":
            car_type_list = car_service._car_repo_seven_seat_suv.get_carlist()
        elif car_type.lower() == "smábíll":
            car_type_list = car_service._car_repo_small_car.get_carlist()

        date_repo = car_service.get_date_repo()
        date_dict = date_repo.get_date_dict()
        for car in car_type_list:
            if car.check_availability(date_list, date_dict, car_type_list):
                return car
        return None

def make_date(a_date):
    new_string = ""
    for letter in a_date:
        if letter in string.digits:
            new_string += letter
    day = new_string[:2]
    month = new_string[2:4]
    year = new_string[4:]
    return date(int(year), int(month), int(day))

def make_date_list(date1, date2):
    date_list = []
    date_to_list = date1
    while date_to_list <= date2:
        date_list.append(date_to_list)
        date_to_list += timedelta(days=1)
    return date_list

    # def update_info(self):
    # choice = ""
    # while choice != 6:
    #     print("Hverju villtu breyta:\n1.  Kennitala\n2.  Flokkur bíls\n3.  Dagsetningar\n4.  Trygging\n5.  Kortanúmer\n6. Bíll")
    #     choice = input()


    #     return Customer(customer_info_list[0],customer_info_list[1],customer_info_list[2],customer_info_list[3],customer_info_list[4])
    