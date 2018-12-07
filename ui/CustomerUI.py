from services.CustomerService import CustomerService
from models.Customer import Customer
from os import system
from models.ui_methods import print_header
from models.ui_methods import make_date

class CustomerMenu:

    def __init__(self, prompt):
        self.__CustomerService = CustomerService()
        self.__prompt = prompt
        self.customer_menu()

    def customer_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma viðskiptavinum við """
        done = False
        while not done:
            print_header(self.__prompt)
            action = input("1.  Leita að viðskiptavin\n2.  Skrá nýjan viðskiptavin\n")
            if action == "1":
                self.__prompt += " / Leita að viðskiptavin"
                print_header(self.__prompt)
                ssn = input("Kennitala: ")
                customer = self.__CustomerService.check_ssn(ssn)
                system('clear')
                print_header(self.__prompt)
                choice = ""
                if customer:
                    while choice is not "4":
                        print(customer)
                        choice = input("\n1.  Sjá pantanir\n2.  Breyta skráningu\n3.  Afskrá viðskiptavin\n4.  Heimasíða\n")
                        if choice == "1":
                            self.__prompt += " / Sjá pantanir"
                            print_header(self.__prompt)
                            #Vantar fall til að sjá pantanir
                        elif choice == "2":
                            self.__prompt += " / Breyta skráningu"
                            print_header(self.__prompt)
                            self.__CustomerService.customer_update_info(customer)
                        elif choice == "3":
                            self.__prompt += " / Afskrá viðskiptavin"
                            print_header(self.__prompt)
                            choice = input("Ertu viss?(j/n): ")
                            if choice == "j":
                                self.__CustomerService.customer_delete(customer)
                                choice = "4"
                else:
                    choice = input('Kennitalan: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\n2.  Heimasíða'.format(ssn))
                    if choice == "2":
                        done = True
            elif action == "2":
                self.__prompt += " / Skrá nýjan viðskiptavin"
                print_header(self.__prompt)
                self.__CustomerService.customer_register()
                done = True