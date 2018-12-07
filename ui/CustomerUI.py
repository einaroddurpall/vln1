from services.CustomerService import CustomerService
from models.Customer import Customer
from os import system
from models.ui_methods import print_header
from models.ui_methods import make_date

class CustomerMenu:

    def __init__(self):
        self.__CustomerService = CustomerService()
        self.customer_menu()

    def customer_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma viðskiptavinum við """
        done = False
        while not done:
            prompt = "Heimasíða / Viðskiptavinir"
            print_header(prompt)
            action = input("1.  Leita að viðskiptavin\n2.  Skrá nýjan viðskiptavin\n3.  Heim\n")
            if action == "1":
                exit_info = ""
                while exit_info == "":
                    prompt += " / Leita að viðskiptavin"
                    print_header(prompt)
                    ssn = input("Kennitala: ")
                    customer = self.__CustomerService.check_ssn(ssn)
                    exit_info2 = ""
                    if customer:
                        while exit_info2 == "":
                            prompt = "Heimasíða / Viðskiptavinir / Leita að viðskiptavin"
                            print_header(prompt)
                            print(customer)
                            choice = input("\n1.  Sjá pantanir\n2.  Breyta skráningu\n3.  Afskrá viðskiptavin\n4.  Tilbaka\n5.  Heim\n")
                            if choice == "1":
                                prompt += " / Sjá pantanir"
                                print_header(prompt)
                                #Vantar fall til að sjá pantanir
                            elif choice == "2":
                                prompt += " / Breyta skráningu"
                                print_header(prompt)
                                self.__CustomerService.customer_update_info(customer)
                            elif choice == "3":
                                prompt += " / Afskrá viðskiptavin"
                                print_header(prompt)
                                choice = input("Ertu viss?(j/n): ")
                                if choice == "j":
                                    self.__CustomerService.customer_delete(customer)
                                    exit_info = "Tilbaka"
                                    exit_info2 = "Tilbaka"
                            elif choice == "4":
                                exit_info = "Tilbaka"
                                exit_info2 = "Tilbaka"
                            else:
                                exit_info = "Heim"
                                exit_info2 = "Heim"
                                done = True
                    else:
                        choice = input('Kennitalan: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\n2.  Tilbaka\n3.  Heim\n'.format(ssn))
                        if choice == "2":
                            exit_info = "Tilbaka"
                        elif choice == "3":
                            exit_info = "Heim"
                            done = True
            elif action == "2":
                prompt += " / Skrá nýjan viðskiptavin"
                print_header(prompt)
                self.__CustomerService.customer_register()
            else:
                done = True