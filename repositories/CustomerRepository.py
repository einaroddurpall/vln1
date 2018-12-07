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

    def update_costumers_list(self):
        with open("./data/customers.csv", "w", encoding = "UTF-8") as customers_file:
            new_file = ""
            for a_customer in self.__customers:
                new_file += a_customer.__repr__() + "\n"
            customers_file.seek(0)
            customers_file.truncate()
            customers_file.write(new_file)

def create_list(self, line_string):
    line_string = line_string.strip("\n")
    line_list = line_string.split(";")
    return line_list