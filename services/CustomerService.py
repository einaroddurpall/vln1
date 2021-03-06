from datetime import datetime
from repositories.CustomerRepository import CustomerRepository
from repositories.OrderRepository import OrderRepository
from services.ChangeService import ChangeService
from models.Customer import Customer

class CustomerService:

    def __init__(self):
        self.__customer_repo = CustomerRepository()
        self.__customers_list = self.__customer_repo.get_customers_list()
        self.__change_service = ChangeService()
        self.__order_repo = OrderRepository()

    def customer_register(self):
        '''fall sem býr til viðskiptavin með grunnuppl. og sendir það síðan í 
        makeÖcustomer fallið til að hægt sé að slá inn réttar uppl um viðskiptain'''
        unique_id = self.__customer_repo.get_unique_id()
        new_customer = Customer(unique_id=unique_id)
        new_customer.make_customer(self.__customer_repo.get_customers_list())
        info_list = new_customer.get_info_list()
        if "t" not in info_list and "h" not in info_list:
            self.__customer_repo.add_customer(new_customer)
            return new_customer
        elif "t" in info_list:
            return "t"
        else:
            return "h"

    def update_order_repo(self):
        '''Fall sem skilar OrderRepository'''
        self.__order_repo = OrderRepository()

    def check_ssn(self, ssn):
        '''Fall sem kíkir hvort kennital stemmir við einhvern af viðskiptavinum sem eru til'''
        for customer in self.__customers_list:
            if customer.get_ssn() == ssn:
                return customer

    def customer_delete(self, customer):
        '''Fall sem tekur inn viðskiptavin og eyðir honum úr listanum og úr skránum'''
        self.__customers_list.remove(customer)
        self.__customer_repo.update_costumers_list()
        self.__change_service.delete_customer_consequences(customer)

    def customer_update_info(self, customer):
        '''Fall sem endurnýjar allar upplýsingar sem eru um ákveðin viðskiptain með að senda
        inn í fallið change_info, síðan endurýjar costomers_listan og sendur síðan í annað fall til að updatea 
        í skránum'''
        old_customer = customer
        customer.customer_change_info(self.__customers_list)
        self.__customer_repo.update_costumers_list()
        #Pæling með pantanir sem eru skráðar á gamla viðskiptavininn
        self.__change_service.change_customer_info_consequences(old_customer, customer)
        
    def customer_get_history(self, customer):
        '''Fall sem nær í ákveðins viðskiptavins verslunar sögu við fyrirtæki og skilar
        allr þær pantanir sem innihalda viðskiptavin í lista'''
        orders = self.__order_repo.get_orders()
        customer_orders = []
        for order in orders:
            if order.get_customer() == customer:
                customer_orders.append(order)
        return customer_orders