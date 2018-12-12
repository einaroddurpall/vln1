from os import system
from time import sleep
from models.Person import Person
from models.Functions import print_header, make_number

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
        return "Nafn: {}\nKennitala: {}\nNotandanafn: {}\nLykilorð: {}\nAðgengi: {}".format(
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
        '''Tekur inn staffÖlist, til þess að passa að starfsmaður sé ekki með sömu kennitölu og annar
        síðan rennur rennur það í gegnum for slaufu þar sem það sendir í fallið change info með mysmunandi verkfni 
        hvert verkefni til að fá uppl. um starfsmann. síðan spyr það hvort all sé rétt ef ekki, þa getur notandi 
        breytt ákveðnum uppl um starfsmann'''
        # Hér er  bara verið að fléttast í gegnum alla verkferla í Change info fallinu til að starfsmaður geti slegið
        # inn allar uppl. sem þarf
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
        # hér er bara verið að gá hvort starfsmaður vilji breyta uppl. sem hann sló inn
        while not done:
            print_header("Heimasíða / Starfsmenn / Skrá nýjan starfsmann")
            print(self)
            print("="*70)
            correct = input("\nEr allt rétt? (j/n) ").lower()
            if correct != "j":
                self.update_info(staff_list)
            else:
                return self
        return False

    def update_info(self, staff_list):
        """Fall sem spyr notanda hvaða uppl. hann vill breyta um starfsmann og sendir síðan á change info fallið
        hvaða upplýsinga notandi vill breyta"""
        correct = False
        while not correct:
            print_header("Heimasíða / Starfsmenn / Skrá nýjan starfsmann / Breyta skráningu")
            print(self)
            print("="*70)
            choice = input("\nHverju villtu breyta:\n1.  Nafn\n2.  Kennitala\n3.  Notandnafn\n4.  Lykilorð\n5.  Breyta aðgangi\n6.  Klára Skráningu\n")
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
        # skráir rétt nafn á starfsmann og gáir ekki hvort það sé í lagi
        if choice == "1":
            self.make_name()
        # skráir rétta kennitölu á starfsmann og gáir hvort kennitaln sé í lagi.
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
        """ spyr hvort starfsmaður eigi að vera með fullan aðgan og skráir það síðan í kerfið"""
        answear = input("Fullt aðgengi að kerfinu (j/n)? ")
        if answear == "j":
            self.__admin = True
        elif answear == "n":
            self.__admin = False

    def make_username(self, texti):
        '''biður notanda um notandanafn og skráir það'''
        username  = input(texti)
        self.__username = username

    def make_password(self, texti):
        '''biður notanda um lykiorð og skráir það'''
        password  = input(texti)
        self.__password = password