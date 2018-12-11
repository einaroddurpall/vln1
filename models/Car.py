import string
from time import sleep
from datetime import date
from models.methods import print_header, error_handle

def make_car_type():
    valid_car_types = ["Fólksbíll", "Smábíll","Fimm sæta jeppi","Sjö sæta jeppi","Smárúta"]
    valid_car_type = False
    while valid_car_type is False:
        number = input("Flokkur bíls: \n1.  Fólksbíll\n2.  Smábíll\n3.  Fimm sæta jeppi\n4.  Sjö sæta jeppi\n5.  Smárúta\n6.  Hætta við\n")
        try:
            number = int(number)
            if number == 6:
                return None
            car_type = valid_car_types[number -1]
            return car_type
        except:
            print("Númerið: {} er ekki í listanum, reyndu aftur.".format(number))

class Car:

    def __init__(self, registration_num="", car_type="", sub_type="", transmission="", milage=0, is_rentable=True):
        self.__registration_num = registration_num
        self.__car_type = car_type
        self.__sub_type = sub_type
        self.__transmission = transmission
        self.__milage = milage
        self.__is_rentable = is_rentable


    def __str__(self):
        return "Bílnúmer: {}\nFlokkur bíls: {}\nTegund bíls {}\n{}\nAkstur: {}\nLaus: {}".format(
        self.__registration_num, self.__car_type, self.__sub_type, self.__transmission, self.__milage, self.__is_rentable)

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
                registration_num = self.check_registration_num(registration_num, all_cars_list)
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
                milage = input("Akstur(km): ")
                try: 
                    int(milage)
                    self.__milage = milage
                    valid_mileage = True
                except: 
                    pass
        #return exit_info

    def check_registration_num(self, registration_num, all_cars_list):
        new_registration_num = ""
        for letter in registration_num:
            if (letter in string.ascii_letters) or (letter in string.digits):
                new_registration_num += letter
        if len(new_registration_num) != 5:
            print("Þetta bílnúmer var ólöglegt, reyndu aftur.")
            return False
        registration_num = new_registration_num.upper()
        if registration_num[0] in string.ascii_letters and registration_num[1] in string.ascii_letters\
        and (registration_num[2] in string.ascii_uppercase or registration_num[2] in string.digits)\
        and registration_num[3] in string.digits and registration_num[4] in string.digits:
            for car in all_cars_list:
                if registration_num == car.get_registration_num():
                    print("Þetta bílnúmer er nú þegar á skrá")
                    return False
            return registration_num
        print("Þetta bílnúmer var ólöglegt, reyndu aftur.")
        return False
                
                





        # done = False
        # while not done:
        #     registration_num = input("Bílnúmer: ")
        #     if registration_num[0] in string.ascii_uppercase and registration_num[1] in string.ascii_uppercase\
        #     and registration_num[2] == "-"\
        #     and (registration_num[3] in string.ascii_uppercase or registration_num[3] in string.digits)\
        #     and registration_num[4] in string.digits and registration_num[5] in string.digits:
        #         break
        #     else:
        #         true_input = False
        #         while true_input != True:
        #             print_header(prompt)
        #             print("Bílnúmerið ", registration_num, " er ekki löglegt bílnúmer.")
        #             choice = input("1.  Reyna aftur\n2.  Tilbaka\n3.  Heim\n")
        #             if choice == "2":
        #                 exit_info = 2
        #                 done = True
        #                 true_input = True
        #             elif choice == "3":
        #                 exit_info = 1
        #                 done = True
        #                 true_input = True
        #             elif choice == "1":
        #                 true_input = True
        #             else:
        #                 print("Ekki löglegur valmöguleiki, reyndu aftur.")
        # if done != True:
        #     car_type = make_car_type()
        #     if car_type == None:
        #         return None
        #     sub_type = input("Tegund bíls: ")
        #     transmission = input("1.  Sjálfskiptur\n2.  Beinskiptur\n")
        #     valid_transmission = False
        #     while valid_transmission is False:
        #         if transmission == "1":
        #             transmission = "Sjálfskiptur"
        #         elif transmission == "2":
        #             transmission = "Beinskiptur"
        #         else:
        #             print("Villa, vinsamlegast veldu sjálfskiptan eða beinskiptan")
        #             transmission = input("1.  Sjálfskiptur\n2.  Beinskiptur\n")
        #             continue
        #         valid_transmission = True
        #     valid_mileage = False
        #     while valid_mileage != True: 
        #         milage = input("Akstur: ")
        #         try: 
        #             int(milage)
        #             valid_mileage = True
        #         except: 
        #             pass
        #     is_rentable = True
        #     new_car = Car(registration_num, car_type, sub_type, transmission, milage, is_rentable)
        #     return new_car
        # return exit_info