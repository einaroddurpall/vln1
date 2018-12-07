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
        self.__OrderService = OrderService()
        self.__prompt = prompt
        self.order_menu()
  
    
    def order_menu(self):
        """ Hér er hægt að framkvæma allar aðgerðir sem koma pöntunum við """
        print_header(self.__prompt)
        action = input("1.  Skoða pöntun\n2.  Skrá nýja pöntun\n3.  Skila bíl\n")
        if action == "1":
            self.__prompt += " / Skoða pöntun"
            print_header(self.__prompt)
            order_name = input("Pöntunarnúmer: ")
            # self.__OrderService
            #Skoða bíl? á þetta ekki að vera skoða pöntun?
        elif action == "2":
            self.__prompt += " / Skrá nýja pöntun"
            print_header(self.__prompt)
            self.__OrderService.make_order_info()
            input("Pöntun skráð.")
            
        elif action == "3":
            self.__prompt += " / Skila bíl"
            print_header(self.__prompt)
            pass