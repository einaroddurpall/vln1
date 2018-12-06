from models.Car import Car

class CarRepository:

    def __init__(self, name):
        self.__name = name
        self.__cars = self.get_cars()

    def add_car(self, car):
        """Bæta bíl í .csv skrá fyrir viðeigandi bílaflokk og í bílalista flokksins"""
        with open("./data/{}.csv".format(self.__name.lower()), "a") as cars_file:
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

    def get_carlist(self):
        return self.__cars