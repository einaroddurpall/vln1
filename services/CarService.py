from repositories.CarRepository import CarRepository
from models.Car import Car
from datetime import datetime

class CarService:

    def __init__(self):
        self.__car_repo_sedan = CarRepository("Sedan")
        self.__car_repo_minibus = CarRepository("Minibus")
        self.__car_repo_seven_seat_suv = CarRepository("seven_seat_suv")
        self.__car_repo_five_seat_suv = CarRepository("five_seat_suv")
        self.__car_repo_small_car = CarRepository("small_car")
        
    
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
        for cars in self.__car_repo_five_seat_suv.get_carlist():
            if cars.get_registration_num() == registration_num:
                return cars
        for cars in self.__car_repo_seven_seat_suv.get_carlist():
            if cars.get_registration_num() == registration_num:
                return cars
        for cars in self.__car_repo_small_car.get_carlist():
            if cars.get_registration_num() == registration_num:
                return cars
        for cars in self.__car_repo_sedan.get_carlist():
            if cars.get_registration_num() == registration_num:
                return cars
        for cars in self.__car_repo_minibus.get_carlist():
            if cars.get_registration_num() == registration_num:
                return cars
        return "Car not found"

        


        