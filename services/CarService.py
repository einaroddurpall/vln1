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
        self.__car_repo_sedan = CarRepository("Sedan")
        self.__car_repo_minibus = CarRepository("Minibus")
        self.__car_repo_seven_seat_suv = CarRepository("seven_seat_suv")
        self.__car_repo_five_seat_suv = CarRepository("five_seat_suv")
        self.__car_repo_small_car = CarRepository("small_car")
        self.__customer_service = CustomerService()
        self.__date_repo = DateRepository()

    def get_date_repo(self):
        return self.__date_repo
        
    def car_register(self, car):
        """Skráir nýjan bíl í kerfið í viðeigandi bílaflokk"""
        car_type = car.get_car_type()
        if car_type.lower() == "sedan":
            self.__car_repo_sedan.add_car(car)
        elif car_type.lower() == "five seat suv":
            self.__car_repo_five_seat_suv.add_car(car)
        elif car_type.lower() == "minibus":
            self.__car_repo_minibus.add_car(car)
        elif car_type.lower() == "seven seat suv":
            self.__car_repo_seven_seat_suv.add_car(car)
        elif car_type.lower() == "small car":
            self.__car_repo_small_car.add_car(car)
    
    def car_find(self, registration_num):
        for car in self.__car_repo_five_seat_suv.get_carlist():
            if car.get_registration_num() == registration_num:
                return car
        for car in self.__car_repo_seven_seat_suv.get_carlist():
            if car.get_registration_num() == registration_num:
                return car
        for car in self.__car_repo_small_car.get_carlist():
            if car.get_registration_num() == registration_num:
                return car
        for car in self.__car_repo_sedan.get_carlist():
            if car.get_registration_num() == registration_num:
                return car
        for car in self.__car_repo_minibus.get_carlist():
            if car.get_registration_num() == registration_num:
                return car
        return "Bíll fannst ekki"
    
    def get_busy_cars(self, date1, date2):
        """Takes in 2 dates and returns a list of all cars that are 
        taken/busy, that day and/or the days between them, returns the cars
        in and dosent repeat the cars."""
        list_of_days = make_date_list(date1, date2)
        car_info_dict = self.__date_repo.get_date_dict()
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


