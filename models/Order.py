class Order:

    def __init__(self, customer="", car="", date_list=[], insurance=""):
        self.__customer = customer
        self.__car = car
        self.__date_list = date_list
        self.__insurance = insurance
    
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

    def __repr__(self):
        return "Order('{}', '{}', '{}', '{}', '{}')".format(
            repr(self.get_customer()), repr(self.get_car()), repr(self.get_first_day()), repr(self.get_last_day()), self.__insurance()
        )

    # def update_info(self):
    # choice = ""
    # while choice != 6:
    #     print("Hverju villtu breyta:\n1.  Kennitala\n2.  Flokkur bíls\n3.  Dagsetningar\n4.  Trygging\n5.  Kortanúmer\n6. Bíll")
    #     choice = input()


    #     return Customer(customer_info_list[0],customer_info_list[1],customer_info_list[2],customer_info_list[3],customer_info_list[4])