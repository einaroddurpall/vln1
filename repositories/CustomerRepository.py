from models.Customer import Customer

class CustomerRepository:

    def __init__(self): 
        """Á eintak af lista með öllum viðskiptavinum."""     
        self.__customers = self.get_customers()

    def add_customer(self, customer):
        """Bæta viðskiptavin í .csv skrá og í viðskiptavinalista"""
        with open("./data/customers.txt", "a", encoding = "UTF-8") as customers_file:
            customers_file.write(customer.__repr__() + '\n')
        self.__customers.append(customer)

    def get_customers(self):
        """Ná í alla viðskiptavini úr skrá."""
        customers = []
        with open("./data/customers.txt", encoding = "UTF-8") as customers_file:
            for row in customers_file.readlines():
                customer = eval(row.strip())
                customers.append(customer)
        return customers
    
    def get_customers_list(self):
        """Skilar lista með öllum viðskiptavinum."""
        return self.__customers

    def update_costumers_list(self):
        """Uppfærir skrá sem heldur utan um viðskiptavi. Kallað er á þetta fall þegar
        lista sem inniheldur alla viðskiptavini er breytt, þ.e. þegar viðskiptavini er breytt.
        Skráin er þá uppfærð í takt við breytingarnar á listanum."""
        with open("./data/customers.txt", "w", encoding = "UTF-8") as customers_file:
            new_file = ""
            for a_customer in self.__customers:
                new_file += a_customer.__repr__() + "\n"
            customers_file.seek(0)
            customers_file.truncate()
            customers_file.write(new_file)

    def get_unique_id(self):
        """Býr til einkennandi númer fyrir hvern viðskiptavin. Með þessari útfærslu opnuðum
        við möguleikann á að breyta kennitölu viðskiptavina."""
        id_list = [customer.get_id() for customer in self.__customers]
        counter = 1
        while True:
            unique_id = "Viðskiptavinur " + str(counter)
            counter += 1
            if unique_id not in id_list:
                return unique_id


def create_list(self, line_string):
    line_string = line_string.strip("\n")
    line_list = line_string.split(";")
    return line_list