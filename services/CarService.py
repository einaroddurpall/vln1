from repositories.CarRepository import CarRepository
from repositories.DateRepository import DateRepository
from services.CustomerService import CustomerService
from models.Car import Car
from datetime import datetime, timedelta

def make_date_list(date1, date2):
    date_list = []
    date_to_list = date1
    while date_to_list <= date2:
        date_list.append(date_to_list)
        date_to_list += timedelta(days=1)
    return date_list

class CarService:

    def __init__(self):
        self._car_repo_sedan = CarRepository("Sedan")
        self._car_repo_minibus = CarRepository("Minibus")
        self._car_repo_seven_seat_suv = CarRepository("seven_seat_suv")
        self._car_repo_five_seat_suv = CarRepository("five_seat_suv")
        self._car_repo_small_car = CarRepository("small_car")
        self._all_cars_list = self.make_all_cars_list()
        self._customer_service = CustomerService()
        self._date_repo = DateRepository()

    def make_all_cars_list(self):
        car_repo_list = [self._car_repo_sedan, self._car_repo_minibus, self._car_repo_seven_seat_suv,
        self._car_repo_five_seat_suv, self._car_repo_small_car]
        all_cars_list = []
        for car_repo in car_repo_list:
            car_type_list = car_repo.get_carlist()
            for car in car_type_list:
                all_cars_list.append(car)
        return all_cars_list

    def make_all_cars_dict(self):
        all_car_dict = {}
        for car in self._all_cars_list:
            car_info_list = [car.get_registration_num(), car.get_sub_type(), car.get_milage(), car.get_transmission()]
            all_car_dict[car.get_car_type()] = all_car_dict.get(car.get_car_type(), []) + [car_info_list]
        return all_car_dict

    def get_all_cars_list(self):
        return self._all_cars_list

    def get_date_repo(self):
        return self._date_repo
        
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
        return "Bíll fannst ekki"
    
    def get_busy_cars(self, date1, date2):
        """Takes in 2 dates and returns a list of all cars that are 
        taken/busy, that day and/or the days between them, returns the cars
        in and dosent repeat the cars."""
        list_of_days = make_date_list(date1, date2)
        car_info_dict = self._date_repo.get_date_dict()
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


