from repositories.CarRepository import CarRepository
from repositories.OrderRepository import OrderRepository
from services.CustomerService import CustomerService
from models.Car import Car, make_car_type
from datetime import datetime, timedelta
from models.methods import print_header, make_date
from services.ChangeService import ChangeService
from time import sleep

def make_date_list(date1, date2):
    date_list = []
    date_to_list = date1
    while date_to_list <= date2:
        date_list.append(date_to_list)
        date_to_list += timedelta(days=1)
    return date_list

def get_car_price(car_type):
    '''Tekur inn streng sem lýsir bíltegundinni og skilar verðið á þeim flokki'''
    if car_type.lower() == "smábíll":
        return CarRepository.SMALL_CAR_PRICE
    elif car_type.lower() == 'fólksbíll':
        return CarRepository.SEDAN_PRICE
    elif car_type.lower() == 'fimm sæta jeppi':
        return CarRepository.FIVE_SEAT_SUV_PRICE
    elif car_type.lower() == 'sjö sæta jeppi':
        return CarRepository.SEVEN_SEAT_SUV_PRICE
    elif car_type.lower() == 'smárúta':
        return CarRepository.MINIBUS_PRICE

class CarService:

    def __init__(self):
        self._car_repo_sedan = CarRepository("Sedan")
        self._car_repo_minibus = CarRepository("Minibus")
        self._car_repo_seven_seat_suv = CarRepository("seven_seat_suv")
        self._car_repo_five_seat_suv = CarRepository("five_seat_suv")
        self._car_repo_small_car = CarRepository("small_car")
        self._all_cars_list = self.make_all_cars_list()
        self._customer_service = CustomerService()
        self._order_repo = OrderRepository()
        self.__change_service = ChangeService()

    def make_all_cars_list(self):
        '''Fall sem nær í alla bíla sem erum í skránum og skilar þeim sem í lista'''
        car_repo_list = [self._car_repo_sedan, self._car_repo_minibus, self._car_repo_seven_seat_suv,
        self._car_repo_five_seat_suv, self._car_repo_small_car]
        all_cars_list = []
        for car_repo in car_repo_list:
            car_type_list = car_repo.get_carlist()
            for car in car_type_list:
                all_cars_list.append(car)
        return all_cars_list

    def make_all_cars_dict(self):
        """fall sem tekur nær i lista af öllum bílum sem eru inn í skránni
        og skilar síðan dictunary sem er með key sem flokk af bíl og síðan 
        info um bílin sem value"""
        all_car_dict = {}
        for car in self._all_cars_list:
            car_info_list = [car.get_registration_num(), car.get_sub_type(), car.get_milage(), car.get_transmission()]
            all_car_dict[car.get_car_type()] = all_car_dict.get(car.get_car_type(), []) + [car_info_list]
        return all_car_dict

    def get_all_cars_list(self):
        return self._all_cars_list

    def get_order_repo(self):
        return self._order_repo
    
    
        
    def car_register(self, car):
        """Skráir nýjan bíl í kerfið í viðeigandi bílaflokk"""
        car_type = car.get_car_type()
        if car_type.lower() == "fólksbíll":
            self._car_repo_sedan.add_car(car)
        elif car_type.lower() == "fimm sæta jeppi":
            self._car_repo_five_seat_suv.add_car(car)
        elif car_type.lower() == "smárúta":
            self._car_repo_minibus.add_car(car)
        elif car_type.lower() == "sjö sæta jeppi":
            self._car_repo_seven_seat_suv.add_car(car)
        elif car_type.lower() == "smábíll":
            self._car_repo_small_car.add_car(car)
        self._all_cars_list.append(car)
    
    def car_find(self, registration_num):
        for car in self._all_cars_list:
            if car.get_registration_num() == registration_num:
                return car
        return False

    def search_for_specific_car(self, a_dict):
        """Function that asks user if he wants to find
        info about specific car type and does so"""
        question = input("Viltu leita af ákveðnari tegund (j/n)? ")
        if question == "j":
            car_type = make_car_type()
            if car_type != None:
                if car_type in a_dict.keys():
                    print("\n{:<15}{:>8} ISK:".format(car_type, get_car_price(car_type)))
                    print("="*60)
                    print("{:>23}{:>10}{:>10}{:>17}".format("Bil tegund", "Bílnúmer", 'Akstur', 'Skipting'))
                    print('-'*60)
                    for car_info in a_dict[car_type]:
                        print("{:>23}{:>10}{:>10}{:>17}".format(car_info[1], car_info[0], car_info[2], car_info[3]))
                    print("="*60)
                    return False
                else:
                    print("Enginn bíll laus í þessari bílategund á þessum tíma")
                    return False

            else:
                return None
        return True

    def print_out_info_for_all_car_types(self, a_dict):
        for key,val in a_dict.items():
            print("\n{:<15}{:>8} ISK:".format(key, get_car_price(key)))
            print("="*60)
            print("{:>23}{:>10}{:>10}{:>17}".format("Bil tegund", "Bílnúmer", 'Akstur', 'Skipting'))
            print('-'*60)
            for car_info in val:
                print("{:>23}{:>10}{:>10}{:>17}".format(car_info[1], car_info[0], car_info[2], car_info[3]))
            print("="*60)

    def print_car_dict(self, a_dict):
        if a_dict:
            statement = self.search_for_specific_car(a_dict)
            if statement:
                self.print_out_info_for_all_car_types(a_dict)
            elif statement == None:
                return True         
        else:
            print("Enginn laus bíll á þessum tíma")

    def get_date_dict(self):
        date_dict = {}
        order_list = self._order_repo.get_order_list()
        for order in order_list:
            order_dates = make_date_list(order.get_first_day(), order.get_last_day())
            car = order.get_car()
            for date in order_dates:
                if date in date_dict:
                    date_dict[date].append(car)
                else:
                    date_dict[date] = [car]
        return date_dict

    def get_busy_cars(self, prompt):
        """Takes in 2 dates and returns a list of all cars that are 
        taken/busy, that day and/or the days between them, returns the cars
        in and dosent repeat the cars."""
        date_found = False
        while not date_found:
            try:
                date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
                date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                if date1 <= date2:
                    date_found = True
                else:
                    print("Villa! Skiladagur getur ekki verið á undan afhendingardegi")
                    sleep(2)
                    print_header(prompt)
            except: 
                print("Vinsamlegast sláðu inn gilda dagsetningu")
                sleep(2)
                print_header(prompt)
        list_of_days = make_date_list(date1, date2)
        car_info_dict = self.get_date_dict()
        car_type_info_dict = {}
        car_licence_list = []
        for date in list_of_days:
            if date in car_info_dict:
                car_list = car_info_dict[date]
                for car in car_list:
                    car_licence = car.get_registration_num()
                    if car_licence not in car_licence_list:
                        car_licence_list.append(car_licence)
                        car_type_info_dict[car.get_car_type()] = car_type_info_dict.get(car.get_car_type(), []) + [[car_licence, car.get_sub_type(), car.get_milage(), car.get_transmission()]]
        return car_type_info_dict

    def get_available_cars(self, prompt):
        car_busy_dict = self.get_busy_cars(prompt)
        all_car_dict = self.make_all_cars_dict()
        delete_key_list = []
        for key in all_car_dict:
            for car in all_car_dict[key]:
                try:
                    if car in car_busy_dict[key]:
                        all_car_dict[key].remove(car)
                        if all_car_dict[key] == []:
                            delete_key_list.append(key)
                except:
                    None
        for key in delete_key_list:
            del all_car_dict[key]
        go_back = self.print_car_dict(all_car_dict)
        return go_back

    def car_get_history(self, car):
        orders = self._order_repo.get_order_list()
        car_orders = []
        for order in orders:
            if order.get_car() == car:
                car_orders.append(order)
        return car_orders

    def car_delete(self, car):
        self._all_cars_list.remove(car)
        car_type = car.get_car_type()
        if car_type == 'smá bíll':
            self._car_repo_small_car.remove_car(car)
        elif car_type == 'fólksbíll':
            self._car_repo_sedan.remove_car(car)
        elif car_type == 'fimm sæta jeppi':
            self._car_repo_five_seat_suv.remove_car(car)
        elif car_type == 'sjö sæta jeppi':
            self._car_repo_seven_seat_suv.remove_car(car)
        elif car_type == 'smárúta':
            self._car_repo_minibus.remove_car(car)