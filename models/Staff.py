from models.Person import Person
from models.Functions import print_header, make_number
from os import system
from time import sleep

class Staff(Person):
    """staff class, is a subclass of the Person class
    takes in name, ssn, username, password and admin. 
    and the name and ssn get's sent to person parent class"""

    def __init__ (self, name = "", ssn = "", username = "", password = "", admin = False):
        Person.__init__(self, name, ssn)
        self.__username = username
        self.__password = password
        self.__admin = admin

    def __repr__(self):
        """Strengur sem sýnir hvernig búa má til eintak af viðeigandi starfsmanni."""
        return "Staff('{}','{}','{}','{}',{})".format(
            self._name, self._ssn, self.__username, self.__password, self.__admin
        )

    def __str__(self):
        """Strengur sem birtist er starfsmaður er prentaður."""
        if self.__admin == True:
            admin = "Kerfisstjórnandi"
        else:
            admin = "Ekki kerifsstjórnandi"
        return "Nafn: {}\nKennitala: {}\nNotandanafn {}\nLykilorð {}\nAðgengi {}".format(
            self._name, self._ssn, self.__username, self.__password, admin
        )
    
    def get_username(self):
        """Skilar notendanafni starfsmanns."""
        return self.__username

    def get_password(self):
        """Skilar lykilorði viðskiptavinar."""
        return self.__password

    def get_admin(self):
        """Skilar True ef starfsmaður er yfirmaður annars False."""
        return self.__admin

    def get_info_list(self):
        """ Skilar lista með upplýsingunum um starfsmanninn"""
        return [self._name, self._ssn, self.__username, self.__password, self.__admin]

    def make_staff(self, staff_list):
        for number in range(1, 6):
            number = str(number)
            self.change_info(number, staff_list)
            info_list = self.get_info_list()
            if "t" in info_list:
                return "t"
            elif "h" in info_list:
                return "h"
            if number == '2':
                if self._ssn == '':
                    done = True
                    break
                else:
                    done = False
        while not done:
            correct = input("Er allt rétt? (j/n) ").lower()
            if correct != "j":
                self.update_info(staff_list)
            else:
                return self
        return False

    def update_info(self, staff_list):
        correct = False
        while not correct:
            print_header("Heimasíða / Starfsmenn / Skrá nýjan starfsmann / Breyta skráningu")
            choice = input("Hverju villtu breyta:\n1.  Nafn\n2.  Kennitala\n3.  Notandnafn\n4.  Lykilorð\n5.  Breyta aðgangi\n6.  Klára Skráningu\n")
            legal_choice = False
            while not legal_choice:
                try:
                    if int(choice) in range(1,7):
                        legal_choice = True
                    else:
                        print("Ekki valmöguleiki, veldu aftur")
                except:
                    print("Ekki valmöguleiki, veldu aftur")
            if choice == "6":
                correct = True
            self.change_info(choice, staff_list)
            print_header("Heimasíða / Starfsmenn / Breyta skráningu")

    def change_info(self, choice, staff_list):
        "Tekur inn upplýsingar til að breyta/búa til starfsmann"
        if choice == "1":
            self.make_name()
        elif choice == "2":
            uniqe_ssn = False
            while not uniqe_ssn:
                uniqe_ssn = True
                change = make_number(10, "Kennitala: ", "Þessi kennitala var ólögleg, reyndu aftur.")
                for staff in staff_list:
                    if staff.get_ssn() == change:
                        print("Það er nú þegar starfsmaður með þessa kennitölu")
                        sleep(2)
                        uniqe_ssn = False
                        break
                if uniqe_ssn == True:
                    self._ssn = change
                else:
                    break  
        elif choice == "3":
            self.make_username('Notandanafn: ')
        elif choice == "4":
            self.make_password('Lykilorð: ')
        elif choice == "5":
            self.make_admin()

    def make_admin(self):
        answear = input("Fullt aðgengi að kerfinu (j/n)? ")
        if answear == "j":
            self.__admin = True
        elif answear == "n":
            self.__admin = False

    def make_username(self, texti):
        username  = input(texti)
        self.__username = username

    def make_password(self, texti):
        password  = input(texti)
        self.__password = password