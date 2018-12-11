from models.Person import Person
from models.Functions import print_header, make_number
from time import sleep

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
        return [self._name, self._ssn, self.__email, self.__gsm, self.__customer_id]

    def make_customer(self, customer_list):
        for number in range(1, 5):
            number = str(number)
            self.change_info(number, customer_list)
            info_list = self.get_info_list()
            for info in info_list:
                if info == "t" or info == "h":
                    return info
        done = False
        while not done:
            correct = input("Er allt rétt? (j/n) ").lower()
            if correct != "j":
                self.customer_change_info(customer_list)
            else:
                done = True

    def customer_change_info(self, customer_list):
        correct = False
        while not correct:
            choice = input("Hverju villtu breyta:\n1. Nafn\n2. Kennitala\n3. Netfang\n4. Símanúmer\n5. Klára Skráningu\n")
            print_header("Heimasíða / Viðskiptavinir / Leita að viðskiptavin / Breyta skráningu")
            legal_choice = False
            while not legal_choice:
                try:
                    if int(choice) in range(1,6):
                        legal_choice = True
                    else:
                        print("Ekki valmöguleiki, veldu aftur")
                except:
                    print("Ekki valmöguleiki, veldu aftur")
            if choice == "5":
                correct = True
            self.change_info(choice, customer_list)
            print_header("Heimasíða / Viðskiptavinir / Leita að viðskiptavin / Breyta skráningu")

    def change_info(self, choice, customer_list):
        if choice == "1":
            self.make_name()
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
        elif choice == "3":
            self.make_email()
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
                else:
                    print("Netfangið {} er ekki löglegt netfang.".format(email))
                    choice = input("1.  Reyna aftur\n2.  Tilbaka\n3.  Heim")
                    if choice == "2":
                        return "Tilbaka"
                    elif choice == "3":
                        return "Heim"
        self.__email = email
