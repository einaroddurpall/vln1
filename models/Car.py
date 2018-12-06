import string

def make_car_type():
    valid_car_types = ["Fólksbíll", "Smábíll","Fimm sæta jeppi","Sjö sæta jeppi","Smárúta",]
    valid_car_type = False
    while valid_car_type is False:
        print("Flokkur bíls:")
        number = input("1.  Fólksbíll\n2.  Smábíll\n3.  Fimm sæta jeppi\n4.  Sjö sæta jeppi\n5.  Smárúta\n")
        try:
            number = int(number)
            car_type = valid_car_types[number -1]
            return car_type
        except:
            print("Error: Númer ekki í listanum, reyndu aftur.")

class Car:

    def __init__(self, registration_num="", car_type="", sub_type="", transmission="", milage=0, is_rentable=True, history=""):
        self.__registration_num = registration_num
        self.__car_type = car_type
        self.__sub_type = sub_type
        self.__transmission = transmission
        self.__milage = milage
        self.__is_rentable = is_rentable

        if history == "":
            self.__history = "Þessi bíll er með enga sögu."
        else: 
            self.__history = history

    def __str__(self):
        return "Bílnúmer: {}\nFlokkur bíls: {}\nTegund bíls {}\n{}\nAkstur: {}\nLaus: {}\nSaga: {}".format(
        self.__registration_num, self.__car_type, self.__sub_type, self.__transmission, self.__milage, self.__is_rentable, self.__history)

    def __repr__(self):
        return "Car('{}','{}','{}','{}',{},{},'{}')".format(self.__registration_num, self.__car_type, self.__sub_type, self.__transmission,
        self.__milage, self.__is_rentable, self.__history)

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
    
    def get_history(self):
        """ Returns the history of the car."""
        return self.__history

    def set_milage(self, milage):
        """ Sets new milage for the car in the system. When the car is returned we need to update the milage for the car."""
        self.__milage = milage

    def set_history(self, order):
        pass

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
    

    def make_car(self):
        while True:
            registration_num = input("Bílnúmer: ")
            if registration_num[0] in string.ascii_uppercase and registration_num[1] in string.ascii_uppercase\
               and registration_num[2] == "-"\
               and (registration_num[3] in string.ascii_uppercase or registration_num[3] in string.digits)\
               and registration_num[4] in string.digits and registration_num[5] in string.digits:
               break
            else:
                print("Bílnúmer er ekki til, vinsamlegast sláðu inn aftur")

        car_type = make_car_type()
        sub_type = input("Tegund bíls: ")
        transmission = input("1.  Sjálfskiptur\n2.  Beinskiptur\n")
        valid_transmission = False
        while valid_transmission is False:
            if transmission == "1":
                transmission = "Sjálfskiptur"
            elif transmission == "2":
                transmission = "Beinskiptur"
            else:
                print("Villa, vinsamlegast veldu sjálfskiptan eða beinskiptan")
                transmission = input("1.  Sjálfskiptur\n2.  Beinskiptur\n")
                continue
            valid_transmission = True
        valid_mileage = False
        while valid_mileage != True: 
            milage = input("Akstur: ")
            try: 
                int(milage)
                valid_mileage = True
            except: 
                pass
        is_rentable = True
        history = ""
        new_car = Car(registration_num, car_type, sub_type, transmission, milage, is_rentable, history)
        return new_car