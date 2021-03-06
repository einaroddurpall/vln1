from os import system
from time import sleep
import string
from services.OrderService import OrderService
from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Functions import print_header, make_date
from models.Order import Order
from ui.OrderUI import OrderUI

class CustomerUI:

    def __init__(self):
        self.__customer_service = CustomerService()
        # self.customer_menu()

    def customer_menu(self):
        """ Hér er hægt að framkvæma tvær aðgerðir sem koma viðskiptavinum við.
            1. Leita að viðskiptavin, hér tekur CustomerService klasinn við kennitölu, athugar hvort það sé til viðskiptavinur
               í kerfinu með þessa kennitölu og skilar viðeigandi viðskiptavin. Þegar viðskiptavinur hefur verið valinn er hann
               sentur í view_customer fallið.
            2. Skrá nýjan viðskiptavin, sjá customer_register í CustomerService klasanum. """
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
                        exit_info, done = self.view_customer(customer)
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
                    exit_info, done = self.view_customer(new_customer)
                elif new_customer == "h":
                    done = True

            else:
                done = True

    def view_customer(self, customer):
        """ Hér er hægt að framkvæma fjórar aðgerðir fyrir viðskiptavin.
            1. Sjá pantanir, hér er hægt að sjá allar pantanir sem þessi viðskiptavinur hefur skráð á sig.
            2. Breyta skráningu, hér er hægt að breyta skráningu viðskiptavinar með hjálp customer_update_info fallinu í CustomerService
               klasanum.
            3. Afskrá viðskiptavin, hér er viðskiptavinurinn tekinn út úr kerfinu og allar þær pantanir sem eru ókláraðar eyðast úr
               kerfinu líka.
            4. Skrá pöntun á viðskiptavin, hér er hoppað beint inn í make_order_info fallið í OrderService klasanum og 
               viðskiptavinurinn líka svo það þurfi ekki að velja hann aftur."""
        loop = True
        while loop:
            prompt = "Heimasíða / Viðskiptavinir / Skoða viðskiptavin"
            print_header(prompt)
            print(customer)
            print('='*70)
            choice = input("\n1.  Sjá pantanir\n2.  Breyta skráningu\n3.  Afskrá viðskiptavin\n4.  Skrá pöntun á viðskiptavin\nt.  Tilbaka\nh.  Heim\n").lower()
            if choice == "1":
                prompt += " / Sjá pantanir"
                print_header(prompt)
                customer_orders = self.__customer_service.customer_get_history(customer)
                if customer_orders:
                    for order in customer_orders:
                        print(order)
                        print()
                    input('Ýttu á "Enter" til að halda áfram: ')
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
                new_order = self.__order_service.make_order_info(prompt, customer)
                if type(new_order) == Order:
                    self.__order_ui = OrderUI()
                    self.__order_ui.view_order(new_order)
                else:
                    if new_order == "h":
                        return "Heim", True

                self.__customer_service.update_order_repo()
            elif choice == "t":
                return "Tilbaka", False
            else:
                return "Heim", True
                
