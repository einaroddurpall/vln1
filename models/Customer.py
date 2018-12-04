from Person import Person

class Customer(Person):

    def __init__ (self,name, ssn, email, gsm, card_info = "", history = ''):
        Person.__init__(self, name, ssn)
        self.__email = email
        self.__gsm = gsm
        self.__card_info = card_info