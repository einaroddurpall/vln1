import data
class CarType:
    def __init__(self, name, price, seats):
        self.__name = name
        self.__price = price
        self.__seats = seats
        self.list_of_cars = []
    
    def get_cars(self):
        with open ("{}.csv".format(self.__name), "r") as f:
            for lines in f:
                resignation_num, sub_type, transmission, car_brand, car_year, 

