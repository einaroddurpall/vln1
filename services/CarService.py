from time import sleep
from os import system
from datetime import datetime, timedelta
from repositories.CarRepository import CarRepository
from repositories.OrderRepository import OrderRepository
from repositories.PriceRepository import PriceRepository
from services.CustomerService import CustomerService
from services.ChangeService import ChangeService
from models.Car import Car
from models.Functions import print_header, make_date, check_registration_num, make_date_list, pretty_str, make_car_type, legal_dates, get_car_price

# def get_car_price(car_type, price_repo):
#     '''Tekur inn streng sem lýsir bíltegundinni og skilar verðið á þeim flokki'''
#     if car_type.lower() == "smábíll":
#         return int(price_repo.get_small_car_price())
#     elif car_type.lower() == 'fólksbíll':
#         return int(price_repo.get_sedan_price())
#     elif car_type.lower() == 'fimm sæta jeppi':
#         return int(price_repo.get_five_seat_suv_price())
#     elif car_type.lower() == 'sjö sæta jeppi':
#         return int(price_repo.get_seven_seat_suv_price())
#     elif car_type.lower() == 'smárúta':
#         return int(price_repo.get_minibus_price())


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
        '''fall sem skilur cars_list'''
        return self._all_cars_list

    def get_order_repo(self):
        '''Fall sem skilar Order repoinu'''
        return self._order_repo

    def make_car(self, prompt):
        ''' Þetta fall býr til bíl með grunn uppl. síðan sendir það í car_change_info fallið að breyta uppl. 
        um hverjn hlut sem þarf að vita um bílin síðan spyr fallið hvort allt í rétt slegið inn, ef ekki sendir fallið
        notanda í fallið change_car_info, þar sem notandi getur breytt viðeigandi uppl.'''
        new_car = Car()
        for step in range(1,6):
            quit_info = new_car.car_change_info(str(step), self._all_cars_list, prompt)
            if type(quit_info) == str:
                return quit_info
        new_car.set_availability(self.get_date_dict())
        print_header(prompt)
        print(new_car)
        print("="*70)
        continue_q = input("\nEr allt rétt? (j/n): ").lower()
        if continue_q != "j":
            self.change_car_info(new_car, True, prompt)
        else:
            self.car_register(new_car)
        return True
        
    def change_car_info(self, car, new_or_not, prompt):
        ''' Ef notandi vill breyta uppl. um bíl þá velur hann hvejru hann bill breyta síðan er sendur í fallið 
        car_change_info til að breyta viðeigandi uppl.'''
        old_car = car
        correct = False
        if new_or_not:
            while not correct:
                print_header(prompt)
                print(car)
                print("="*70)
                print("\nHverju viltu breyta:\n1.  Bílnúmeri\n2.  Bílaflokkur\n3.  Undirtegund\n4.  Skipting\n5.  Akstur(km)\n6.  Klára Skráningu")
                legal_choice = False
                while not legal_choice:
                    choice = input()
                    try:
                        if int(choice) in range(1,7):
                            legal_choice = True
                        else:
                            print("Ekki valmöguleiki, veldu aftur")
                    except:
                        print("Ekki valmöguleiki, veldu aftur")
                if choice == "6":
                    correct = True
                car.car_change_info(choice, self._all_cars_list, prompt)
        # ef bílinn er ekki nýr og breyta er verið gömlu bíl þá fer hann notandi hingað
        else: 
            while not correct:
                print_header(prompt)
                print(car)
                print("="*70)
                print("\nHverju viltu breyta:\n1.  Undirtegund\n2.  Skipting\n3.  Akstur(km)\n4.  Klára Skráningu")
                legal_choice = False
                while not legal_choice:
                    choice = input()
                    try:
                        if int(choice) in range(1,5):
                            legal_choice = True
                            choice = str(int(choice) + 2)
                        else:
                            print("Ekki valmöguleiki, veldu aftur")
                    except:
                        print("Ekki valmöguleiki, veldu aftur")
                if choice == "6":
                    correct = True
                car.car_change_info(choice, self._all_cars_list, prompt)
        if new_or_not:
            self.car_register(car)
            self._all_cars_list.append(car)
        else:
            self.update_car_list(car)
            self.__change_service.change_car_info_consequences(old_car, car)

    
        
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

    def update_car_list(self, car):
        """Skráir nýjan bíl í kerfið í viðeigandi bílaflokk"""
        car_type = car.get_car_type()
        if car_type.lower() == "fólksbíll":
            self._car_repo_sedan.update_car_list(car)
        elif car_type.lower() == "fimm sæta jeppi":
            self._car_repo_five_seat_suv.update_car_list(car)
        elif car_type.lower() == "smárúta":
            self._car_repo_minibus.update_car_list(car)
        elif car_type.lower() == "sjö sæta jeppi":
            self._car_repo_seven_seat_suv.update_car_list(car)
        elif car_type.lower() == "smábíll":
            self._car_repo_small_car.update_car_list(car)
        
    
    def car_find(self, registration_num):
        '''Þetta fall skila bílnum með því bílnumeri sem er sent inn ef bíll er til'''
        registration_num = check_registration_num(registration_num)
        if registration_num:
            for car in self._all_cars_list:
                if car.get_registration_num() == registration_num:
                    return car, True
            return False, True
        return False, False

    def search_for_specific_car_type(self, a_dict, condition):
        """Function that asks user if he wants to find
        info about specific car type and does so"""
        question = input("Viltu leita af ákveðinni tegund (j/n)? ")
        if question == "j":
            car_type = make_car_type()
            if car_type in a_dict.keys():
                print("\n{:<18}{:>10}:".format(car_type, pretty_str(get_car_price(car_type, PriceRepository()), "ISK")))
                print("="*70)
                print("{:>20}{:>10}{:>13}{:>17}".format("Biltegund", "Bílnúmer", 'Akstur', 'Skipting'))
                print('-'*70)
                for car_info in a_dict[car_type]:
                    car_number = car_info[0]
                    print("{:>20}{:>6}-{}{:>13}{:>17}".format(car_info[1], car_number[0:2],car_number[2:], pretty_str(car_info[2], "km"), car_info[3]))
                print("="*70)
                return False
            else:
                if condition == False:
                    print("Enginn bíll laus í þessari bílategund á þessum tíma")
                elif condition == True:
                    print("Enginn bíll í útleigu í þessari bílategund á þessum tíma")
                return False
        return True

    def print_out_info_for_all_car_types(self, a_dict):
        '''Fall sem prentar út upplýsingum um alla bíla dictionerynu og undir hvaða bílaflokki þeir eru'''
        price_repo = PriceRepository()
        for key,val in a_dict.items():
            print("\n{:<18}{:>10}:".format(key, pretty_str(get_car_price(key, price_repo), "ISK")))
            print("="*70)
            print("{:>20}{:>10}{:>13}{:>17}".format("Bil tegund", "Bílnúmer", 'Akstur', 'Skipting'))
            print('-'*70)
            for car_info in val:
                car_number = car_info[0]
                print("{:>20}{:>6}-{}{:>13}{:>17}".format(car_info[1], car_number[0:2],car_number[2:], pretty_str(car_info[2], "km"), car_info[3]))
            print("="*70)

    def print_car_dict(self, a_dict, condition):
        '''fall sem sendir í föll til að prenta út lista af bílunum sem notandi vill fá sjá'''
        if a_dict:
            statement = self.search_for_specific_car_type(a_dict, condition)
            if statement:
                self.print_out_info_for_all_car_types(a_dict)
        else:
            print("Enginn bíll í útleigu á þessum tíma")

    def get_date_dict(self):
        '''Býr til tómt date_dict og sækir upplýsingar um pantanir niður í order_repo. Skoðar hverja pöntun fyrir 
        sig og sækir alla daga hverrar pöntunar. Dagarnir verða keys í dictionaryinu en bílar pantana verða value.
        Hver dagur sem inniheldur einhverja pöntun er þannig skráður sem key í dictinu og valueið er listi af öllum
        bílum sem eru bókaðir þann dag.'''
        date_dict = {}
        order_list = self._order_repo.get_orders()
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
        date1, date2 = legal_dates(prompt)
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
        """Fær uppflettilista með uppteknum bílum, fær svo uppflettilista með öllum bílum, finnur svo þá bíla 
        sem eru sameiginlegir í báðum listum og fjarlægir þá úr uppflettilistanum með öllum bílum"""
        car_busy_dict = self.get_busy_cars(prompt)
        all_car_dict = self.make_all_cars_dict()
        delete_key_list = []
        for key in car_busy_dict:
            for car in car_busy_dict[key]:
                try:
                    if car in car_busy_dict[key]:
                        all_car_dict[key].remove(car)
                        if all_car_dict[key] == []:
                            delete_key_list.append(key)
                except:
                    None
        for key in delete_key_list:
            del all_car_dict[key]
        self.print_car_dict(all_car_dict, False)

    def car_get_history(self, car):
        '''Fall sem nær í lista af öllum pöntunum sem ákveðinn bíll hefur komið í'''
        orders = self._order_repo.get_orders()
        car_orders = []
        for order in orders:
            if order.get_car() == car:
                car_orders.append(order)
        return car_orders

    def car_delete(self, car):
        '''fall sem eyðir ákveðnum bíl úr bílategunds listanum sem hann er í og 
        eyðir honum úr skránum með að senda ákveðnar uppl niður í car_repoið'''
        self._all_cars_list.remove(car)
        car_type = car.get_car_type().lower()
        if car_type == 'smábíll':
            self._car_repo_small_car.remove_car(car)
        elif car_type == 'fólksbíll':
            self._car_repo_sedan.remove_car(car)
        elif car_type == 'fimm sæta jeppi':
            self._car_repo_five_seat_suv.remove_car(car)
        elif car_type == 'sjö sæta jeppi':
            self._car_repo_seven_seat_suv.remove_car(car)
        elif car_type == 'smárúta':
            self._car_repo_minibus.remove_car(car)
        self.__change_service.delete_car_consequences(car, self, self._customer_service)
