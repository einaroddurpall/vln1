from services.CustomerService import CustomerService
from models.Customer import Customer
from os import system
from time import sleep
from models.Functions import print_header, make_date
import string
from services.OrderService import OrderService

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
            action = input("1.  Leita að viðskiptavin\n2.  Skrá nýjan viðskiptavin\nh.  Heim\n")
            if action == "1":
                exit_info = ""
                prompt += " / Leita að viðskiptavin"
                while exit_info == "":
                    print_header(prompt)
                    ssn = input("Kennitala: ").lower()
                    if ssn == "h":
                        done = True
                        break
                    elif ssn == "t":
                        break
                    customer = self.__customer_service.check_ssn(ssn)
                    if customer:
                        exit_info, done = self.view_customer(customer, prompt)
                    else:
                        choice = input('Kennitalan: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\nt.  Tilbaka\nh.  Heim\n'.format(ssn))
                        if choice == "t":
                            break
                        elif choice == "h":
                            done = True
                            break
            elif action == "2":
                prompt += " / Skrá nýjan viðskiptavin"
                print_header(prompt)
                new_customer = self.__customer_service.customer_register()
                if type(new_customer) == Customer:
                    exit_info, done = self.view_customer(new_customer, prompt)
                elif new_customer == "h":
                    done = True

            else:
                done = True

    def view_customer(self, customer, prompt):
        exit_info2 = ""
        while exit_info2 == "":
            prompt = "Heimasíða / Viðskiptavinir / Skoða viðskiptavin"
            print_header(prompt)
            print(customer)
            choice = input("\n1.  Sjá pantanir\n2.  Breyta skráningu\n3.  Afskrá viðskiptavin\n4.  Skrá Pöntun á viðskiptavin\nt.  Tilbaka\nh.  Heim\n").lower()
            if choice == "1":
                prompt += " / Sjá pantanir"
                print_header(prompt)
                customer_orders = self.__customer_service.customer_get_history(customer)
                if customer_orders:
                    for order in customer_orders:
                        print(order)
                        print()
                    input("Ýttu á enter til að halda áfram: ")
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
                    return "Tilbaka", False
            elif choice == "4":
                prompt += " / Skrá pöntun á viðskiptavin"
                print_header(prompt)
                self.__order_service = OrderService()
                self.__order_service.make_order_info(prompt, customer)
                self.__customer_service.update_order_repo()
            elif choice == "t":
                return "Tilbaka", False
            else:
                return "Heim", True
                
