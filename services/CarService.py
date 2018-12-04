from repositories.CarRepository import CarRepository
from models.Car import Car
class CarService:

    def __init__(self):
        self.__car_repo_sedan = CarRepository("Sedan")
        self.__car_repo_minibus = CarRepository("Minibus")
        self.__car_repo_seven_seat_suv = CarRepository("seven_seat_suv")
        self.__car_repo_five_seat_suv = CarRepository("five_seat_suv")
        self.__car_repo_small_car = CarRepository("small_car")
        
    
    def car_register(self, car):
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
        


