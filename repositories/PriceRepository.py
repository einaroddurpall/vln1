import csv

class PriceRepository:

    def __init__(self):
        
        self.__price_list = self.read_car_prices()
        self.__small_car_price, self.__sedan_price, self.__five_seat_suv_price, self.__seven_seat_suv_price, self.__minibus_price = self.__price_list

    def get_small_car_price(self):
        return self.__small_car_price[1]
    
    def get_sedan_price(self):
        return self.__sedan_price[1]

    def get_five_seat_suv_price(self):
        return self.__five_seat_suv_price[1]
    
    def get_seven_seat_suv_price(self):
        return self.__seven_seat_suv_price[1]
    
    def get_minibus_price(self):
        return self.__minibus_price[1]
    
    def set_small_car_price(self, new_price):
        self.__small_car_price[1] = new_price
    
    def set_sedan_price(self, new_price):
        self.__sedan_price[1] = new_price

    def set_five_seat_suv_price(self, new_price):
        self.__five_seat_suv_price[1] = new_price
    
    def set_seven_seat_suv_price(self, new_price):
        self.__seven_seat_suv_price[1] = new_price
    
    def set_minibus_price(self, new_price):
        self.__minibus_price[1] = new_price

    def read_car_prices(self):
        the_list = []
        with open ("./data/price.csv", encoding = "UTF-8") as price_file:
            dict_reader_dicts = csv.DictReader(price_file)
            for row in dict_reader_dicts:
                the_list.append([row["car_type"],row["price"]])
        return the_list
    
    def update_price_list(self):
        with open ("./data/price.csv", "w", encoding = "UTF-8") as price_file:
            price_file.write("car_type,price\n")
            for price in self.__price_list:
                price_file.write(price[0] + "," + price[1] + "\n")


# price_repo = PriceRepository()
# price_repo.set_sedan_price("1")
# price_repo.update_price_list()