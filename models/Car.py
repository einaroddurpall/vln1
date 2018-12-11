import string
from time import sleep
from datetime import date
from models.Functions import print_header, error_handle, check_registration_num, pretty_str, make_car_type

class Car:

    def __init__(self, registration_num="", car_type="", sub_type="", transmission="", milage=0, is_rentable=True):
        self.__registration_num = registration_num
        self.__car_type = car_type
        self.__sub_type = sub_type
        self.__transmission = transmission
        self.__milage = milage
        self.__is_rentable = is_rentable

    def __str__(self):
        return "Bílnúmer: {}-{}\nFlokkur bíls: {}\nTegund bíls {}\n{}\nAkstur: {}\nLaus: {}".format(
        self.__registration_num[0:2], self.__registration_num[2::], self.__car_type, self.__sub_type, self.__transmission,pretty_str(self.__milage, "km"), self.__is_rentable)

    def __repr__(self):
        return "Car('{}','{}','{}','{}',{},{})".format(self.__registration_num, self.__car_type, self.__sub_type, self.__transmission,
        self.__milage, self.__is_rentable)

    def get_registration_num(self):
        """ Returns the registration number of the car."""
        return self.__registration_num

    def get_car_type(self):
        """ Returns the car type of the car."""
        return self.__car_type

    def get_sub_type(self):
        """ Returns the sub type of the car."""
        return self.__sub_type
    
    def get_transmission(self):
        """ Returns the transmission of the car."""
        return self.__transmission

    def get_milage(self):
        """ Returns the milage of the car."""
        return self.__milage
    
    def get_is_rentable(self):
        """ Returns if the car is rentable or not."""
        return self.__is_rentable

    def set_milage(self, milage):
        """ Sets new milage for the car in the system. When the car is returned we need to update the milage for the car."""
        self.__milage = milage

    def check_availability(self, date_list, date_dict, car_list):
        is_rentable = True
        for date in date_list:
            if date in date_dict:
                for car in date_dict[date]:
                    if self == car:
                        is_rentable = False
                        break
        return is_rentable

    def __eq__(self, other):
        return self.get_registration_num() == other.get_registration_num()

    def car_change_info(self, step, all_cars_list):
        if step == "1":
            done = False
            while not done:
                registration_num = input("Bílnúmer: ")
                registration_num = check_registration_num(registration_num)
                for car in all_cars_list:
                    if registration_num == car.get_registration_num():
                        print("Þetta bílnúmer er nú þegar á skrá")
                        registration_num = False
                if registration_num:
                    self.__registration_num = registration_num
                    done = True
        elif step == "2":
            self.__car_type = make_car_type()
            if self.__car_type == None:
                return None
        elif step == "3":
            self.__sub_type = input("Tegund bíls: ")
        elif step == "4":
            valid_transmission = False
            while valid_transmission is False:
                transmission = input("1.  Sjálfskiptur\n2.  Beinskiptur\n")
                if transmission == "1":
                    self.__transmission = "Sjálfskiptur"
                    valid_transmission = True
                elif transmission == "2":
                    self.__transmission = "Beinskiptur"
                    valid_transmission = True
                else:
                    print("Villa, vinsamlegast veldu sjálfskiptan eða beinskiptan")
        elif step == "5":
            valid_mileage = False
            while valid_mileage != True: 
                milage = input("Akstur (km): ")
                try: 
                    int(milage)
                    self.__milage = milage
                    valid_mileage = True
                except: 
                    print('Vinsamlegast sláðu inn réttan akstursvegalengd bíl.')