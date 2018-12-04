from Person import Person

class Customer(Person):

    def __init__ (self,name, ssn, email, gsm, card_info = "", history = ''):
        Person.__init__(self, name, ssn)
        self.__email = email
        self.__gsm = gsm
        self.__card_info = card_info
    
def main():
    Kristjan = Customer("Kristjan", "0220982349", "Stjanihot@hotmail.com", "8451289")
    print(Kristjan)

main()