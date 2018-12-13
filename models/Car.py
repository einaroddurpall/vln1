import string
from time import sleep
from datetime import date
from models.Functions import print_header, error_handle, check_registration_num, pretty_str, make_car_type

class Car:

    def __init__(self, registration_num="", car_type="", sub_type="", transmission="", milage=0):
        """Hver bíll hefur bílnúmer, tegund, undirtegund, skiptingu og akstur."""
        self.__registration_num = registration_num
        self.__car_type = car_type
        self.__sub_type = sub_type
        self.__transmission = transmission
        self.__milage = milage


    def __str__(self):
        """Strengur sem birtist er bíll er prentaður."""
        if self.__is_available:
            is_available = "Bíllinn er laus í dag"
        else:
            is_available = "Bíllinn er ekki laus í dag"
        return "{}\n".format(self.__car_type) + "-"*70 + "\n{:<15} {:>18}-{}\n{:<15} {:>22}\n{:<15} {:>22}\n{:<15} {:>22}\n{:<15} {:>22}\n{:<15} {:>22}".format(
        "Bílnúmer:", self.__registration_num[0:2], self.__registration_num[2::], "Flokkur bíls:", self.__car_type, 
        "Tegund bíls:", self.__sub_type, "Skipting", self.__transmission, "Akstur:", pretty_str(self.__milage, "km"), "Laus:", is_available)

    def __repr__(self):
        """Strengur sem sýnir hvernig búa má til eintak af viðeigandi bíl."""
        return "Car('{}','{}','{}','{}',{})".format(self.__registration_num, self.__car_type, self.__sub_type, self.__transmission,
        self.__milage)

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

    def set_milage(self, milage):
        """ Sets new milage for the car in the system. When the car is returned we need to update the milage for the car."""
        self.__milage = milage
    
    def set_availability(self, date_dict):
        """sendir inn í checkabailability fallið upplýsingar og skilar hvort bílinn sé laus á þeim degi"""
        if self.check_availability([date.today()], date_dict, self.get_car_type):
            self.__is_available = True
        else:
            self.__is_available = False

    def check_availability(self, date_list, date_dict, car_list):
        """Tekur við lista af dögum, dictionary sem heldur utan um hvaða bílar eru bókaðir á hverjum degi og lista
        af bílum af ákveðnum flokki. Fallið athugar hvort bíllinn (self) er laus fyrir alla dagana í listanum og
        skilar True eða False."""
        is_rentable = True
        for date in date_list:
            if date in date_dict:
                for car in date_dict[date]:
                    if self == car:
                        is_rentable = False
                        break
        return is_rentable

    def __eq__(self, other):
        """Tveir bílar eru sami bíllinn ef þeir hafa sama bílnúmer."""
        return self.get_registration_num() == other.get_registration_num()

    def car_change_info(self, step, all_cars_list, prompt):
        '''þetta fall tekur inn uppl. um bíl og hvaða uppl. notandi vill breyta um bílin, 
        síðan fer í viðeigandi skref og breytir þeim með viðeigandi uppl sem fallið hefur eða 
        spyr notandann um upplýsingar og breytir þeim'''
        # biður um bílnum frá notanda gáir síðan hvort bílnúmerið sé í lagi og skráir síðan bílnumerið á bílin ef það er löglegt
        if step == "1":
            done = False
            while not done:
                print_header(prompt)
                registration_num = input("Bílnúmer: ")
                if registration_num.lower() == "h" or registration_num.lower() == "t":
                    return registration_num
                registration_num = check_registration_num(registration_num)
                for car in all_cars_list:
                    if registration_num == car.get_registration_num():
                        print("Villa: Þetta bílnúmer er nú þegar á skrá")
                        sleep(2)
                        registration_num = False
                if registration_num:
                    self.__registration_num = registration_num
                    done = True
        # biður um hvernig bílatýpu bílinn er og skráir það á bílin
        elif step == "2":
            self.__car_type = make_car_type()
        # Biður um hvernig Tegund bíllinn er og skráir þáð síðan á bílin
        elif step == "3":
            self.__sub_type = input("Tegund bíls: ")
            if self.__sub_type == "t" or self.__sub_type == "h":
                return self.__sub_type
        # spyr um hvernig skipting bílinn er með og skráir það síðan á instancið
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
                elif transmission == "t" or transmission == "h":
                    return transmission
                else:
                    print("Villa, vinsamlegast veldu sjálfskiptan eða beinskiptan")
        # spyr um hvað bílinn er ekinn mikið og skráir það síðan á bílin og gáir síðan hvort það sérétt slegið inn
        elif step == "5":
            valid_mileage = False
            while valid_mileage != True: 
                milage = input("Akstur (km): ")
                if milage == "t" or milage == "h":
                    return milage
                try: 
                    int(milage)
                    self.__milage = milage
                    valid_mileage = True
                except: 
                    print('Vinsamlegast sláðu inn rétta akstursvegalengd bíls.')
