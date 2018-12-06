from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer
from datetime import datetime

class CustomerService:

    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def customer_register(self):
        new_customer = Customer()
        new_customer.make_customer(self.__customer_repo.get_customers_list())
        self.__customer_repo.add_customer(new_customer)

    def get_customer_list(self):
        return self.__customer_repo.get_customers()

    def check_ssn(self, ssn):
        customers = self.get_customer_list()
        for customer in customers:
            if customer.get_ssn() == ssn:
                return customer

    def customer_delete(self, ssn):
        self.__customer_repo.remove_customer(ssn)

    def customer_update_info(self, customer):
        customers_list = self.__customer_repo.get_customers_list()
        new_customer = customer.customer_change_info(customers_list)
        self.customer_delete(customer.get_ssn())
        self.__customer_repo.add_customer(new_customer)
        # Pæling með pantanir sem eru skráðar á gamla viðskiptavininn