class Order:

<<<<<<< HEAD
    def __init__(self, ssn="", date_list=[], insurance="", card_info="", car=""):
        self.__ssn = ssn
        self.__date_list = date_list
        self.__insurance = insurance
        self.__card_info = card_info
        self.__car = car
=======
    def __init__(self, customer="", car="", date_list=[], insurance="", card_info=""):
        self.__customer = customer
        self.__car = car
        self.__date_list = date_list
        self.__insurance = insurance
        self.__card_info = card_info
>>>>>>> afb8243ec8cb9e2acd404b736b77ebd25c576ac6
    
    def get_ssn(self):
        return self.__ssn

    def get_date_list(self):
        return self.__date_list

    def get_insurance(self):
        return self.__insurance

<<<<<<< HEAD
    def get_card_infro(self):
        return self.__card_info

    def get_car(self):
        return self.__car
=======
    def get_card_info(self):
        return self.__card_info

    def __repr__(self):
        return "Order('{}', '{}', '{}', '{}', '{}', '{}')".format(
            repr(self.get_customer()), repr(self.get_car()), repr(self.get_first_day()), repr(self.get_last_day()), self.get_insurance(), self.get_card_info()
        )
>>>>>>> afb8243ec8cb9e2acd404b736b77ebd25c576ac6

    # def update_info(self):
    # choice = ""
    # while choice != 6:
    #     print("Hverju villtu breyta:\n1.  Kennitala\n2.  Flokkur bíls\n3.  Dagsetningar\n4.  Trygging\n5.  Kortanúmer\n6. Bíll")
    #     choice = input()


    #     return Customer(customer_info_list[0],customer_info_list[1],customer_info_list[2],customer_info_list[3],customer_info_list[4])