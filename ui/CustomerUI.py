from services.CustomerService import CustomerService
from models.Customer import Customer
from os import system
from time import sleep
from models.methods import print_header, make_date

class CustomerMenu:

    def __init__(self):
        self.__customer_service = CustomerService()
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
                prompt += " / Leta að viðskiptavin"
                while exit_info == "":
                    print_header(prompt)
                    ssn = input("Kennitala: ")
                    customer = self.__customer_service.check_ssn(ssn)
                    exit_info2 = ""
                    if customer:
                        prompt += " / Leita að viðskiptavin"
                        while exit_info2 == "":
                            print_header(prompt)
                            print(customer)
                            choice = input("\n1.  Sjá pantanir\n2.  Breyta skráningu\n3.  Afskrá viðskiptavin\n4.  Tilbaka\n5.  Heim\n")
                            if choice == "1":
                                prompt += " / Sjá pantanir"
                                print_header(prompt)
                                customer_orders = self.__customer_service.customer_get_history(customer)
                                if customer_orders:
                                    for order in customer_orders:
                                        print(order)
                                else:
                                    print("Þessi viðskiptavinur hefur enga notkunarsögu.")
                                    sleep(2)
                            elif choice == "2":
                                prompt += " / Breyta skráningu"
                                print_header(prompt)
                                self.__customer_service.customer_update_info(customer)
                            elif choice == "3":
                                prompt += " / Afskrá viðskiptavin"
                                print_header(prompt)
                                choice = input("Ertu viss?(j/n): ")
                                if choice == "j":
                                    self.__customer_service.customer_delete(customer)
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
                new_customer = self.__customer_service.customer_register()
                if type(new_customer) == str:
                    done = True
            else:
                done = True