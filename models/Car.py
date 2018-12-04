class Car:

    def __init__(self, registration_num, car_type, sub_type, transmission, milage=0, is_rentable=True, history=""):
        self.__registration_num = registration_num
        self.__sub_type = sub_type
        self.__transmission = transmission
        self.__milage = milage
        self.__is_rentable = is_rentable

        if history == "":
            self.__history = "This car has no history of rental."
        else: 
            self.__history = history

        valid_car_type = False
        while valid_car_type is False:
            if car_type == "Sedan":
                self.__car_type = car_type
            elif car_type == "SUV":
                self.__car_type = car_type
            elif car_type == "Small car":
                self.__car_type = car_type
            elif car_type == "Minibus":
                self.__car_type = car_type
            else:
                print('Error: Car type: "{}" not found, car types are case sensetive.'.format(car_type))
                car_type = input("Enter car type: ")
                continue
            valid_car_type = True

    def __str__(self):
        return "Registration number: {}\nCar type: {}\nType {}\nTransmission: {}\nMilage: {}\nIs rentable: {}\nHistory: {}".format(
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

    def check_availability(self, date1, date2):
        pass