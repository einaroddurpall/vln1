class Car:
    def __init__(self, registration_num="", car_type="", sub_type="", transmission="", milage=0, is_rentable=True, history=""):
        self.__registration_num = registration_num
        self.__car_type = car_type
        self.__sub_type = sub_type
        self.__transmission = transmission
        self.__milage = milage
        self.__is_rentable = is_rentable
        
        if history == "":
            self.__history = "This car has no history of rental."
        else: 
            self.__history = history

        if car_type == "Sedan":
            self.__price = 15000
        elif car_type == "SUV":
            self.__price = 20000
        elif car_type == "Small car":
            self.__price = 10000
        elif car_type == "Minibus":
            self.__price = 30000
        else:
            print("Error: Car type not found.")

    def __str__(self):
        return "Registration number: {}\nCar type: {}\nType {}\nTransmission: {}\nMilage: {}\nIs rentable: {}\nHistory: {}".format(
            self.__registration_num, self.__car_type, self.__sub_type, self.__transmission, self.__milage, self.__is_rentable, self.__history
        )

    def get_registration_num(self):
        return self.__registration_num

    def get_car_type(self):
        return self.__car_type

    def get_sub_type(self):
        return self.__sub_type

    def set_registration_num(self, registration_num):
        self.__registration_num = registration_num

    def set_history(self, order):
        pass