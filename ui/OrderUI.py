from services.OrderService import OrderService
from models.Order import Order
from os import system
from time import sleep
from models.methods import print_header

class OrderMenu:
    def __init__(self):
        self.__order_service = OrderService()
        self.order_menu()

    def order_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma pöntunum við """
        done = False
        while not done:
            prompt = "Heimasíða / Skoða eða skrá pantanir"
            print_header(prompt)
            action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Skila bíl\n4.  Heim\n")
            if action == "1":
                prompt += " / Skoða pöntun"
                print_header(prompt)
                exit_info = ""
                while exit_info == "":
                    order_name = input("Pöntunarnúmer: ")
                    order = self.__order_service.get_order_by_name(order_name)
                    print_header(prompt)
                    choice = ""
                    if order:
                        while choice == "":
                            prompt = "Heimasíða / Skoða eða skrá pantanir / Skoða pöntun"
                            print(order)
                            print('='*60)
                            choice = input("\n1.  Uppfæra pöntun\n2.  Eyða pöntun\n3.  Tilbaka\n4.  Heim\n")
                            if choice == "1":
                                prompt += " / Uppfæra Pöntun"
                                print_header(prompt)
                                self.__order_service.change_order_info(order, False)
                            elif choice == "2":
                                prompt += " / Eyða pöntun"
                                print_header(prompt)
                                choice = input("Ertu viss? (j/n): ")
                                if choice == "j":
                                    self.__order_service.order_delete(order)
                                    choice = "Tilbaka"
                                    exit_info = "Tilbaka"
                            elif choice == "3":
                                choice = "Tilbaka"
                                exit_info = "Tilbaka"
                            else:
                                choice = "Heim"
                                exit_info = "Heim"
                                done = True
                    else:
                        choice = input('Pöntunin: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\n2.  Tilbaka\n3.  Heimasíða\n'.format(order_name))
                        if choice == "2":
                            exit_info = "Tilbaka"
                        elif choice == "3":
                            exit_info = "Heim"
                            done = True
            elif action == "2":
                prompt += " / Skrá nýja pöntun"
                print_header(prompt)
                new_order = self.__order_service.make_order_info()
                if new_order == "Tilbaka":
                    None
                elif new_order == "Heim":
                    done = True
                else: 
                    print("Pöntun skráð.")
                    sleep(2)
            
            elif action == "3":
                prompt += " / Skila bíl"
                print_header(prompt)
                pass
            else:
                done = True