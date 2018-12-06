from models.Customer import Customer

class CustomerRepository:

    def __init__(self):      
        self.__customers = self.get_customers()

    def add_customer(self, customer):
        """Bæta viðskiptavin í .csv skrá og í viðskiptavinalista"""
        with open("./data/customers.csv", "a", encoding = "UTF-8") as customers_file:
            customers_file.write(customer.__repr__() + '\n')
        self.__customers.append(customer)

    def get_customers(self):
        """Ná í alla viðskiptavini"""
        customers = []
        with open("./data/customers.csv", encoding = "UTF-8") as customers_file:
            for row in customers_file.readlines():
                customer = eval(row.strip())
                customers.append(customer)
        return customers
    
    def get_customers_list(self):
        return self.__customers