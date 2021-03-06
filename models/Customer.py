from time import sleep
from models.Person import Person
from models.Functions import print_header, make_number

class Customer(Person):
    """Customer class, is a subclass of the Person class
    takes in name, ssn. email, gsm, history
    and the name and ssn get's sent to person parent class"""

    def __init__ (self, unique_id, name="", ssn="", email="", gsm=""):
        Person.__init__(self, name, ssn)
        self.__email = email
        self.__gsm = gsm
        self.__customer_id = unique_id
        
    def get_id(self):
        """Skilar einkennandi númeri viðskiptavins, id, sem forritið hefur skaffað."""
        return self.__customer_id

    def get_email(self):
        """Skilar netfangi viðskiptavinar."""
        return self.__email

    def get_gsm(self):
        """Skilar símanúmeri viðskiptavinar."""
        return self.__gsm

    def __eq__(self, other):
        """Tveir viðskiptavinir eru sami einstaklingur ef þeir hafa sama einkennandi númer, id."""
        return self.get_id() == other.get_id()

    def __repr__(self):
        """Strengur sem sýnir hvernig búa má til eintak af viðeigandi viðskiptavin."""
        return "Customer('{}','{}','{}','{}','{}')".format(
            self.__customer_id, self._name, self._ssn, self.__email, self.__gsm
        )

    def __str__(self):
        """Strengur sem birtist er viðskiptavinur er prentaður."""
        return "Nafn: {}\nKennitala: {}\nNetfang: {}\nSími: {}".format(
            self._name, self._ssn, self.__email, self.__gsm
        )

    def get_info_list(self):
        '''skilar lista sem er með öllum upllýsingum sem hver viðskiptavinur hefur '''
        return [self._name, self._ssn, self.__email, self.__gsm, self.__customer_id]

    def make_customer(self, customer_list):
        '''Tekur inn customer_list, til þess að passa að viðskiptavinurinn sé ekki með sömu kennitölu og annar
        síðan rennur rennur það í gegnum for slaufu þar sem það sendir í fallið change info með mysmunandi verkfni 
        hvert verkefni til að fá uppl. um viðskiptavin. síðan spyr það hvort all sé rétt ef ekki, þa getur notandi 
        breytt ákveðnum uppl um viðskiptavin'''
        # Hér er  bara verið að fléttast í gegnum alla verkferla í Change info fallinu til hægt sé að slá
        # inn allar uppl. sem þarf
        for step in range(1, 5):
            self.change_info(str(step), customer_list)
            info_list = self.get_info_list()
            for info in info_list:
                if info == "t" or info == "h":
                    return info
        done = False
        # hér er bara verið að gá hvort viljað er að breyta uppl. sem slegið var inn
        while not done:
            print_header("Heimasíða / Viðskiptavinir / Skrá nýjan viðskiptavin")
            print(self)
            print("="*70)
            correct = input("\nEr allt rétt? (j/n) ").lower()
            if correct != "j":
                self.customer_change_info(customer_list)
            else:
                done = True

    def customer_change_info(self, customer_list):
        """Fall sem spyr notanda hvaða uppl. hann vill breyta um viðskiptavin og sendir síðan á change info fallið
        hvaða upplýsinga notandi vill breyta"""
        correct = False
        while not correct:
            legal_choice = False
            while not legal_choice:
                print_header("Heimasíða / Viðskiptavinir / Leita að viðskiptavin / Breyta skráningu")
                print(self)
                print("="*70)
                choice = input("\nHverju villtu breyta:\n1. Nafn\n2. Kennitala\n3. Netfang\n4. Símanúmer\n5. Klára Skráningu\n")
                print_header("Heimasíða / Viðskiptavinir / Leita að viðskiptavin / Breyta skráningu")
                try:
                    if int(choice) in range(1,6):
                        legal_choice = True
                        if choice == "5":
                            correct = True
                        else:
                            self.change_info(choice, customer_list)
                            print_header("Heimasíða / Viðskiptavinir / Leita að viðskiptavin / Breyta skráningu")
                    else:
                        print("Ekki valmöguleiki, veldu aftur")
                except:
                    print("Ekki valmöguleiki, veldu aftur")

    def change_info(self, choice, customer_list):
        '''Fallið fær um hvað upplýsingum þarf að breyta um viðskiptavin og sendir hann i gegnum þann feril
        og villu prófar þannig að notandi getur aðeins slegið inn réttar uppl.'''
        #hér fær notandi að breyta nafni viðskiptavinars og gáð hvort það sé löglegt nafn
        if choice == "1":
            self.make_name()
        # Hér er breytt kennitölu notnadna og gáð hvort það sé rétt sleið
        elif choice == "2":
            uniqe_ssn = False
            while not uniqe_ssn:
                uniqe_ssn = True
                change = make_number(10, "Kennitala: ", "Þessi kennitala var ólögleg, reyndu aftur.")
                for customer in customer_list:
                    if customer.get_ssn() == change:
                        print("Það er nú þegar viðskiptavinur með þessa kennitölu")
                        uniqe_ssn = False
            self._ssn = change
        # Hér er breytt nafni emails og síðn gáð hvort það er rétt slegið inn
        elif choice == "3":
            self.make_email()
        # hér er breytt símanúmer viðskiptavins og gáð hvort það sér löglegt
        elif choice == "4":
            change = make_number(7, "Símanúmer: ", "Þetta símanúmer var ólöglegt, reyndu aftur.")
            self.__gsm = change

    def make_email(self):
        """Fall sem leiðir notanda í gegnum það ferli að skrá netfang viðskiptavinar. Netfangið
        verður að hafa @ merki og lén."""
        legal_email = False
        while not legal_email:
            email = input("Netfang: ")
            email_split = email.split("@")
            if len(email_split) == 2:
                domain = email_split[1]
                domain_list = domain.split(".")
                if len(domain_list) == 2:
                    legal_email = True
            if not legal_email:
                print("Netfangið {} er ekki löglegt netfang.".format(email))
                choice = input("1.  Reyna aftur\nt.  Tilbaka\nh.  Heim\n").lower()
                if choice == "t":
                    return "Tilbaka"
                elif choice == "h":
                    return "Heim"
        self.__email = email
