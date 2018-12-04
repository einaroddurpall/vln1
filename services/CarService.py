from repositories.CarRepository import CarRepository

class CarService:

    def __init__(self):
        pass
    
    def register_car(self, registration_number, car_type,
                    sub_type, transmission, milage):
        new_car = Car(registration_number, car_type, sub_type, transmission, milage)
        car_type.add_car(new_car)