class OrderRepsitory:

    def __init__(self):
        self.__order_list = []
        self.get_orders()
    
    def get_orders(self):
        """Setur pantanir í lista"""
        with open("./data/orders.csv") as order_file:
            for row in order_file:
                order = eval(row.strip)
                self.__order_list.append(order)
    
    def add_order(self, order):
        """Bætir við pöntun í pöntunarskjalið"""
        with open("./data/order.csv", "a") as order_file:
            order_file.write(order.__repr__() + '\n')
        self.__order_list.append(order)
    
    



