from services.OrderService import OrderService
from models.Order import Order
from os import system
from time import sleep
from models.Functions import print_header, pretty_str

class OrderMenu:
    def __init__(self):
        self.__order_service = OrderService()


    def order_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma pöntunum við """
        done = False
        while not done:
            prompt = "Heimasíða / Skoða eða skrá pantanir"
            print_header(prompt)
            action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Klára pantanir dagsins\nh.  Heim\n")
            if action == "1":      # Bæta við að það sé hægt að skrifa 1 í staðinn fyrir Order 1
                prompt += " / Skoða pöntun"
                print_header(prompt)
                exit_info = ""
                while exit_info == "":
                    order_name = input("Pöntunarnúmer: ")
                    if order_name == "t":
                        break
                    elif order_name == "h":
                        done = True
                        break
                    order = self.__order_service.get_order_by_name(order_name)
                    print_header(prompt)
                    choice = ""
                    if order:
                        while choice == "":
                            prompt = "Heimasíða / Skoða eða skrá pantanir / Skoða pöntun"
                            print(order)
                            print('='*60)
                            choice = input("\n1.  Uppfæra pöntun\n2.  Eyða pöntun\nt.  Tilbaka\nh.  Heim\n")
                            if choice == "1":       #Pöntun uppfærist í csv næst þegar kerfið er opnað
                                prompt += " / Uppfæra Pöntun"
                                self.__order_service.change_order_info(order, False, prompt)
                                exit_info = "Pöntun uppfærð"
                            elif choice == "2":
                                prompt += " / Eyða pöntun"
                                print_header(prompt)
                                choice = input("Ertu viss? (j/n): ")
                                if choice == "j":
                                    self.__order_service.order_delete(order)
                                    choice = "Tilbaka"
                                    exit_info = "Tilbaka"
                            elif choice == "t":
                                choice = "Tilbaka"
                                exit_info = "Tilbaka"
                            else:
                                choice = "h"
                                exit_info = "Heim"
                                done = True
                    else:
                        choice = input('Pöntunin: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\nt.  Tilbaka\nh.  Heimasíða\n'.format(order_name))
                        if choice == "t" or choice == "h":
                            if choice == "h":
                                done = True
                            exit_info = "Tilbaka"
            elif action == "2":
                finished = False
                while not finished:
                    prompt = "Heimasíða / Skoða eða skrá pantanir / Skrá nýja pöntun"
                    print_header(prompt)
                    new_order = self.__order_service.make_order_info(prompt, False)
                    if type(new_order) != Order:
                        if new_order == "t":
                            finished = True
                        elif new_order == "h":
                            finished = True
                            done = True
                    else:
                        print_header(prompt)
                        choice = input("1.  Skrá aðra pöntun\nt.  Tilbaka\nh.  Heim\n")
                        if choice == "t" or choice == "h":
                            if choice == "h":
                                done = True
                            finished = True
            elif action == "3":
                prompt += " / Klára pantanir dagsins"
                print_header(prompt)
                choice = self.__order_service.complete_orders(prompt)
                if choice == "h":
                    done = True
            else:
                done = True