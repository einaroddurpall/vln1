class Order:

    def __init__(self, ssn="", car_type="", date_list=[], insurance="", card_info="", car=""):
        self.__ssn = ssn
        self.__car_type = car_type
        self.__date_list = date_list
        self.__insurance = insurance
        self.__card_info = card_info
        self.__car = car
    
    def get_ssn(self):
        return self.__ssn

    def get_car_type(self):
        return self.__car_type

    def get_date_list(self):
        return self.__date_list

    def get_insurance(self):
        return self.__insurance

    def get_card_infro(self):
        return self.__card_info

    def get_car(self):
        return self.__car

    # def update_info(self):
    # choice = ""
    # while choice != 6:
    #     print("Hverju villtu breyta:\n1.  Kennitala\n2.  Flokkur bíls\n3.  Dagsetningar\n4.  Trygging\n5.  Kortanúmer\n6. Bíll")
    #     choice = input()


    #     return Customer(customer_info_list[0],customer_info_list[1],customer_info_list[2],customer_info_list[3],customer_info_list[4])