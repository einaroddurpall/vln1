from Person import Person

class Customer(Person):
    """Customer class, is a subclass of the Person class
    takes in name, ssn. email, gsm, card_info, history
    and the name and ssn get's sent to person parent class"""

    def __init__ (self,name, ssn, email, gsm, card_info = "", history = ''):
        Person.__init__(self, name, ssn)
        self.__email = email
        self.__gsm = gsm
        self.__card_info = card_info
        self.__history = history
    
    def update_cutomer_info (self, history):
        """function that creates a history or adds
        new history to the old one with an enter between it"""
        self.__history += history + "\n"

    def show_history(self):
        """Prints out the history"""
        return self.__history