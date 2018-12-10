from models.Car import Car


class CarRepository:
    SMALL_CAR_PRICE = 10000
    SEDAN_PRICE = 15000
    FIVE_SEAT_SUV_PRICE = 20000
    SEVEN_SEAT_SUV_PRICE = 25000
    MINIBUS_PRICE = 30000

    def __init__(self, name):
        self.__name = name
        self.__cars = self.get_cars()

    def add_car(self, car):
        """Bæta bíl í .csv skrá fyrir viðeigandi bílaflokk og í bílalista flokksins"""
        with open("./data/{}.csv".format(self.__name.lower()), "a", encoding = "UTF-8") as cars_file:
            cars_file.write(car.__repr__() + '\n')
        self.__cars.append(car)

    def get_cars(self):
        """Ná í alla bíla úr viðeigandi bílaflokk"""
        cars = []
        with open("./data/{}.csv".format(self.__name.lower()), encoding = "UTF-8") as cars_file:
            for row in cars_file.readlines():
                car = eval(row.strip())
                cars.append(car)
        return cars

    def update_car_list(self):
        with open("./data/{}.csv".format(self.__name), "w", encoding = "UTF-8") as car_type_file:
            new_file = ""
            for car in self.__cars:
                new_file += car.__repr__() + "\n"
            car_type_file.seek(0)
            car_type_file.truncate()
            car_type_file.write(new_file)
    
    def remove_car(self, car):
        self.__cars.remove(car)
        self.update_car_list()


    def get_carlist(self):
        return self.__cars