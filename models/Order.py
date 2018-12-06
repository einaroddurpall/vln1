class Order:

    def __init__(self, ssn="", car_type="", date_list=[], insurance="", card_info=""):
        self.__ssn = ssn
        self.__car_type = car_type
        self.__date_list = date_list
        self.__insurance = insurance
        self.__card_info = card_info
    
    def get_ssn(self):
        return self.__ssn

    def get_car_type(self):
        return self.__car_type

    def get_date_list(self):
        return self.__date_list

    def get_insurance(self):
        return self.__insurance

    def get_car_infro(self):
        return self.__card_info

    def update_info(self):
        pass