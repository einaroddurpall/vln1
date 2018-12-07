from services.OrderService import OrderService
from models.Order import Order
from os import system

def print_header(prompt=""):
    """ Hreinsar terminal og prentar út header með slóð """
    system('clear')
    print("Heimasíða", end="")
    print(prompt)
    print("="*40)

class OrderMenu:
    def __init__(self, prompt):
        self.__order_service = OrderService()
        self.__prompt = prompt
        self.order_menu()
  
    
    def order_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma pöntunum við """
        done = False
        while not done:
            print_header(self.__prompt)
            action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Skila bíl\n")
            if action == "1":
                self.__prompt += " / Skoða pöntun"
                print_header(self.__prompt)
                order_name = input("Pöntunarnúmer: ")
                order = self.__order_service.get_order_by_name(order_name)
                system('clear')
                print_header(self.__prompt)
                choice = ""
                if order:
                    while choice is not "3":
                        print(order)
                        choice = input("\n1.  Uppfæra pöntun\n2.  Eyða pöntun\n3.  Heimasíða\n")
                        if choice == "1":
                            self.__prompt += " / Uppfæra Pöntun"
                            print_header(self.__prompt)
                            self.__order_service.change_order_info(order, False)
                        elif choice == "2":
                            self.__prompt += " / Eyða pöntun"
                            print_header(self.__prompt)
                            choice = input("Ertu viss?(j/n): ")
                            if choice == "j":
                                self.__order_service.order_delete(order)
                                choice = "3"
                else:
                        choice = input('Pöntunin: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\n2.  Heimasíða'.format(order_name))
                        if choice == "2":
                            done = True
                # self.__order_service
                #Skoða bíl? á þetta ekki að vera skoða pöntun?
            elif action == "2":
                self.__prompt += " / Skrá nýja pöntun"
                print_header(self.__prompt)
                self.__order_service.make_order_info()
                input("Pöntun skráð.")
            
            elif action == "3":
                self.__prompt += " / Skila bíl"
                print_header(self.__prompt)
                pass