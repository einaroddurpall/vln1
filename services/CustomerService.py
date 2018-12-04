from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer

class CustomerService:

    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def customer_register(self, customer):
        self.__customer_repo.add_customer(customer)