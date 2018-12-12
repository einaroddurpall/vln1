import string
from datetime import datetime, timedelta, date
from os import system
from time import sleep
from models.Functions import make_number, make_date_list, make_date, pretty_str, make_car_type, legal_dates, print_header, pretty_date
from models.Car import Car

class Order:
    def __init__(self, customer="", car="", date_list=[], insurance="", card_info="", order_name="", order_price = 0, complete = False):
        """Hver pöntun hefur viðskiptavin, bíl, lista af dögum, tryggingu, kortaupplýsingar(sem tryggingu), pöntunarnúmer/nafn, 
        verð og upplýsingar um hvort hún er búin eða ekki."""
        self.__customer = customer
        self.__car = car
        self.__date_list = date_list
        self.__insurance = insurance
        self.__card_info = card_info
        self.__order_name = order_name
        self.__order_price = order_price
        self.__complete = complete
    
    def get_customer(self):
        """Skilar viðskiptavin pöntunarinnar."""
        return self.__customer

    def get_first_day(self):
        """Skilar fyrsta dag pöntunarinnar."""
        return self.__date_list[0]

    def get_last_day(self):
        """Skilar síðasta dag pöntunarinnar."""
        return self.__date_list[-1]

    def get_car(self):
        """Skilar bíl pöntunarinnar."""
        return self.__car

    def get_date_list(self):
        """Skilar öllum dögum pöntunarinnar."""
        return self.__date_list

    def get_insurance(self):
        """Skilar tryggingaupplýsingum pöntunarinnar."""
        return self.__insurance

    def get_card_info(self):
        """Skilar kortaupplýsingum viðskiptavinar pöntunarinnar."""
        return self.__card_info

    def get_order_name(self):
        """Skilar pöntunarnafni pöntunarinnar."""
        return self.__order_name
    
    def get_order_price(self):
        """Skilar verði pöntunarinnar."""
        return self.__order_price

    def get_order_complete(self):
        """Skilar upplýsingum um hvort pöntun sé lokið."""
        return self.__complete

    def set_order_name(self, name):
        """Tekur við einkennandi nafni og setur það sem nafn pöntunar."""
        self.__order_name = name

    def set_customer(self, customer):
        """Tekur við  viðskiptavin og skráir hann sem viðskiptavin pöntunarinnar."""
        self.__customer = customer

    def set_car(self, car):
        """Tekur við  bíl og setur hann sem bíl pöntunarinnar."""
        self.__car = car
    
    def set_complete(self, statement):
        """Tekur við boolean gildi og setur það sem upplýsingar um hvort pöntun sé kláruð."""
        self.__complete = statement

    def __eq__(self, other):
        """Tvær pantanir eru sama pöntunin ef þær hafa sama pöntunarnúmer."""
        return self.get_order_name() == other.get_order_name()

    def __repr__(self):
        """Strengur sem sýnir hvernig búa má til eintak af viðeigandi pöntun."""
        return "{};{};{};{};{};{};{};{};{}".format(
            str(self.get_order_name()),repr(self.get_customer()), repr(self.get_car()), repr(self.get_first_day()), 
            repr(self.get_last_day()), self.get_insurance(), self.get_card_info(), self.get_order_price(), self.get_order_complete()
        )
    
    def __str__(self):
        """Strengur sem birtist er pöntun er prentuð."""
        return "{}\n".format(self.__order_name) + "-"*60 + "\n" + "{:<18} {}\n{:<18} {}\n{:<18} {}\n{:<18} {}\n{:<18} {}\n{:<18} {}\n{:<18} {}\n{:<18} {}".format(
             "Viðskiptavinur:", self.__customer.get_name(), "Bíll:", self.__car.get_registration_num(), 
            "Afendingardagur:", pretty_date(str(self.get_first_day())), "Skiladagur:", pretty_date(str(self.get_last_day())), 
            "Trygging:", self.__insurance, "Kortanumer:", self.__card_info, "Verð:",pretty_str(self.get_order_price(), "ISK"), "Pöntun lokið:", self.get_order_complete()
        )
    
    def set_price(self, price):
        """sets the price of the orders"""
        self.__order_price = price

    # def get_info_list(self):
    #     return [self.__ss]

    def change_info(self, step, car_service, customer_service, prompt = ""):
        if step == "1":
            valid_ssn = False
            while valid_ssn is not True:
                ssn = input("Kennitala viðskiptavinar: ")
                if ssn == "t" or ssn == "h":
                    return ssn
                self.__customer = customer_service.check_ssn(ssn)
                if self.__customer:
                    valid_ssn = True
                else:
                    choice = input("Kennitalan {} fannst ekki.\n1.  Reyna aftur\nt.  Tilbaka\nh.  Heim\n".format(ssn))
                    if choice == "t" or choice == "h":
                        return choice
        elif step == "2":
            step2 = False
            while step2 is not True:
                car_type = make_car_type()
                date1, date2 = legal_dates(prompt)
                self.__date_list = make_date_list(date1, date2)
                self.__car = self.rent_car(car_type, self.__date_list, car_service)
                if self.__car:
                    step2 = True
                    print_header(prompt)
                else:
                    print("Enginn bíll laus með þessi skilyrði")
                    sleep(2)
                    print_header(prompt)
        elif step == "3":
            step3 = False
            while step3 is not True:
                number = input("Veldu tryggingu:\n1.  Grunntrygging\n2.  Aukatrygging\n")
                if number == "2":
                    self.__insurance = "Aukatrygging"
                    step3 = True
                elif number == "1":
                    self.__insurance = "Grunntrygging"
                    step3 = True
                elif number == "t" or number == "h":
                    return number
                else:
                    print("Vinsamlegast veldu viðurkennt gildi")
        elif step == "4":
            self.__card_info = make_number(16, "Kortanúmer: ", "Ólöglegt kortanúmer, reyndu aftur.")
                #"Order " + str(self.__order_num))
                #self.__order_num += 1

    def rent_car(self, car_type, date_list, car_service):
        """ Þetta fall tekur á móti car_type og date_list, býr til carlist fyrir viðeigandi car_type og athugar hvort einhver
            bíll í þessum carlist sé laus á dögunum í date_list."""
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

        date_dict = car_service.get_date_dict()
        for car in car_type_list:
            if car.check_availability(date_list, date_dict, car_type_list):
                return car
        return None