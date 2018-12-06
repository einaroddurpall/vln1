from models.Person import Person

class Customer(Person):
    """Customer class, is a subclass of the Person class
    takes in name, ssn. email, gsm, card_info, history
    and the name and ssn get's sent to person parent class"""

    def __init__ (self,name="", ssn="", email="", gsm="", card_info="", history = ""):
        Person.__init__(self, name, ssn)
        self.__email = email
        self.__gsm = gsm
        self.__card_info = card_info
        
        if history == "":
            self.__history = "Þessi viðskiptavinur hefur aldrei tekið bíl á leigu."
        else: 
            self.__history = history

    def get_email(self):
        return self.__email

    def get_gsm(self):
        return self.__gsm

    def get_card_info(self):
        return self.__card_info
    
    def update_cutomer_info (self, history):
        """function that creates a history or adds
        new history to the old one with an enter between it"""
        self.__history += history + "\n"

    def show_history(self):
        """Prints out the history"""
        return self.__history

    def __repr__(self):
        return "Customer('{}','{}','{}','{}','{}','{}')".format(
            self._name, self._ssn, self.__email, self.__gsm, self.__card_info, self.__history
        )

    def __str__(self):
        return "Customer name: {}, SSN: {}, email: {}, gsm: {}, credit card information: {}, history: {}".format(
            self._name, self._ssn, self.__email, self.__gsm, self.__card_info, self.__history
        )

    def make_customer(self):
        customer_info_list = ["","","","",""]
        customer_info_list[0] = make_name()
        customer_info_list[1] = input("Kennitala: ")
        customer_info_list[2] = input("Netfang: ")
        customer_info_list[3] = input("Símanúmer: ")
        customer_info_list[4] = input("Kortanúmer: ")
        correct = input("Er allt rétt? (j/n) ").lower()
        if correct != "j":
            choice = ""
            while choice != 6:
                print("Hverju villtu breyta:\n1. Nafn\n2. Kennitala\n3. Netfang\n4. Símanúmer\n5. Kortanúmer\n6. Klára Skráningu")
                choice = input()

        return Customer(customer_info_list[0],customer_info_list[1],customer_info_list[2],customer_info_list[3],customer_info_list[4])

def make_name():
    legal_name = False
    while not legal_name:
        inp = input("Nafn: ")
        for letter in inp:
            try:
                int(letter)
                print("Nafnið inniheldur ólöglega stafi")
                legal_name = False
                break
            except:
                legal_name = True
    return inp

def make_ssn():
    legal_ssn = False
    while not legal_ssn:
        inp = input("Kennitala: ")
        ssn = ""
        for letter in inp:
            try:
                int(letter)
                ssn += letter
            except:
                continue
        if len(ssn) == 10:
            legal_ssn = True
        else:
            print("Kennitalan er ekki lögleg, reyndu aftur")
    return ssn

def make_email():
    legal_email = False
    while not legal_email:
        inp = input("Netfang: ")
        email = inp.split("@")
        if len(email) == 2:
            domain = email[1]
            domain_list = domain.split(".")
            if len(domain_list) == 2:
                legal_email = True
    return inp

