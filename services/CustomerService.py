from repositories.CustomerRepository import CustomerRepository
from models.Customer import Customer
from datetime import datetime
from services.ChangeService import ChangeService

class CustomerService:

    def __init__(self):
        self.__customer_repo = CustomerRepository()
        self.__customers_list = self.__customer_repo.get_customers_list()
        self.__change_service = ChangeService()

    def customer_register(self):
        new_customer = Customer()
        new_customer.make_customer(self.__customer_repo.get_customers_list())
        self.__customer_repo.add_customer(new_customer)

    def check_ssn(self, ssn):
        for customer in self.__customers_list:
            if customer.get_ssn() == ssn:
                return customer

    def customer_delete(self, customer):
        self.__customers_list.remove(customer)
        self.__customer_repo.update_costumers_list()

    def customer_update_info(self, customer):
        old_customer = customer
        customer.customer_change_info(self.__customers_list)
        self.__customer_repo.update_costumers_list()
        #Pæling með pantanir sem eru skráðar á gamla viðskiptavininn
        self.__change_service.change_customer_info_consequences(old_customer, customer)
        