from models.Person import Person
from models.Person import make_number
from models.ui_methods import print_header

class Customer(Person):
    """Customer class, is a subclass of the Person class
    takes in name, ssn. email, gsm, history
    and the name and ssn get's sent to person parent class"""

    def __init__ (self, unique_id, name="", ssn="", email="", gsm="", history=""):
        Person.__init__(self, name, ssn)
        self.__email = email
        self.__gsm = gsm
        self.__customer_id = unique_id
        self.__history = history
        
        if history == "":
            self.__history = "Þessi viðskiptavinur hefur aldrei tekið bíl á leigu."
        else: 
            self.__history = history

    
    def get_id(self):
        return self.__customer_id

    def get_email(self):
        return self.__email

    def get_gsm(self):
        return self.__gsm

    def update_customer_history (self, history):
        """function that creates a history or adds
        new history to the old one with an enter between it"""
        self.__history += history + "\n"

    def show_history(self):
        """Prints out the history"""
        return self.__history

    def __eq__(self, other):
        return self.get_ssn() == other.get_ssn()

    def __repr__(self):
        return "Customer('{}','{}','{}','{}','{}','{}')".format(
            self.__customer_id, self._name, self._ssn, self.__email, self.__gsm, self.__history
        )

    def __str__(self):
        return "Nafn: {}\nKennitala: {}\nNetfang: {}\nSími: {}\nSaga: {}".format(
            self._name, self._ssn, self.__email, self.__gsm, self.__history
        )

    def make_customer(self, customer_list):
        for number in range(1, 5):
            number = str(number)
            self.change_info(number, customer_list)
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
                    print("Ólöglegt netfang, reyndu aftur.")
        self.__email = email
