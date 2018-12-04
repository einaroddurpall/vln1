from Person import Person

class Customer(Person):
    """Customer class, is a subclass of the Person class
    takes in name, ssn, email, gsm, card_info, history
    and the name and ssn are sent to the person parent class"""

    def __init__ (self,name, ssn, email, gsm, card_info = "", history = ""):
        Person.__init__(self, name, ssn)
        self.__email = email
        self.__gsm = gsm
        self.__card_info = card_info
        
        if history == "":
            self.__history = "This car has no history of rental."
        else: 
            self.__history = history

    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn

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
            self.__name, self.__ssn, self.__email, self.__gsm, self.__card_info, self.__history
        )

    def __str__(self):
        return "Customer name: {}, SSN: {}, email: {}, gsm: {}, credit card information: {}, history: {}".format(
            self.__name, self.__ssn, self.__email, self.__gsm, self.__card_info, self.__history
        )