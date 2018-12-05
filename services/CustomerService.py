from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer
from datetime import datetime

class CustomerService:

    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def customer_register(self, customer):
        self.__customer_repo.add_customer(customer)

    def get_customer_list(self):
        return self.__customer_repo.get_customers()

    def check_ssn(self, ssn):
        customers = self.get_customer_list()
        for customer in customers:
            if customer.get_ssn() == ssn:
                return customer
        return 'Viðskiptavinur er ekki í kerfinu.'