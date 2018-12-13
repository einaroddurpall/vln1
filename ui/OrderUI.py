from os import system
from time import sleep
from services.OrderService import OrderService
from models.Order import Order
from models.Functions import print_header, pretty_str

class OrderUI:
    def __init__(self):
        self.__order_service = OrderService()
        self.order_menu()

    def order_menu(self):
        """ Hér er hægt að framkvæma þrjár aðgerðir sem koma pöntunum við.
            1. Skoða pöntun, hér þarf að setja inn pöntunarnúmer og OrderService klasinn athugar hvort það sé til pöntun með
               þessu númeri og skilar viðeigandi pöntun. Þegar pöntun hefur verið valin er hægt að framkvæma tvær aðgerðir, annað
               hvort uppfæra upplýsingar hennar eða afskrá hana.
            2. Skrá nýja pöntun, fer beint í fallið make_order_info í OrderService klasanum.
            3. Klára pantanir dagsins fer í fallið complete_orders í Orderservice klasanum. """
        done = False
        while not done:
            prompt = "Heimasíða / Skoða eða skrá pantanir"
            print_header(prompt)
            action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Klára pantanir dagsins\nh.  Heim\n")
            if action == "1":
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
                    if order:
                        exit_info, done = self.view_order(order)
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
                    if type(new_order) == Order:
                        finished, done = self.view_order(new_order)
                    else:
                        if new_order == "t":
                            finished = True
                        elif new_order == "h":
                            finished = True
                            done = True
            elif action == "3":
                prompt += " / Klára pantanir dagsins"
                print_header(prompt)
                choice = self.__order_service.complete_orders(prompt)
                if choice == "h":
                    done = True
            else:
                done = True

    def view_order(self, order):
        loop = True
        while loop:
            prompt = "Heimasíða / Skoða eða skrá pantanir / Skoða pöntun"
            print_header(prompt)
            print(order)
            print('='*60)
            choice = input("\n1.  Uppfæra pöntun\n2.  Eyða pöntun\nt.  Tilbaka\nh.  Heim\n")
            if choice == "1":
                prompt += " / Uppfæra Pöntun"
                self.__order_service.change_order_info(order, prompt)
                # exit_info = "Pöntun uppfærð"
            elif choice == "2":
                prompt += " / Eyða pöntun"
                print_header(prompt)
                choice = input("Ertu viss? (j/n): ")
                if choice == "j":
                    self.__order_service.order_delete(order)
                    return "Tilbaka", False
            elif choice == "t":
                return "Tilbaka", False
            else:
                return "Heim", True