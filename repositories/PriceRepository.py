import csv

class PriceRepository:

    def __init__(self):
        
        self.__price_list = self.read_car_prices()
        self.__small_car_price, self.__sedan_price, self.__five_seat_suv_price,\
        self.__seven_seat_suv_price, self.__minibus_price ,self.__base_insurance_price, self.__extra_insurance_price = self.__price_list

    def get_price_list(self):
        """Skilar lista sem inniheldur 7 tveggja staka lista, hver þeirra með nafn af verðinu og verðið sjálft"""
        return self.__price_list

    def get_small_car_price(self):
        """Skilar verði á smábíl sem str"""
        return self.__small_car_price[1]
    
    def get_sedan_price(self):
        """Skilar verði á fólksbíl sem str"""
        return self.__sedan_price[1]

    def get_five_seat_suv_price(self):
        """Skilar verði á fimm sæta jeppa sem str"""
        return self.__five_seat_suv_price[1]
    
    def get_seven_seat_suv_price(self):
        """Skilar verði á sjö sæta jeppa sem str"""
        return self.__seven_seat_suv_price[1]
    
    def get_minibus_price(self):
        """Skilar verði á smárútu sem str"""
        return self.__minibus_price[1]
    
    def get_base_insurance_price(self):
        """Skilar verði á grunntryggingu sem str"""
        return self.__base_insurance_price[1]

    def get_extra_insurance_price(self):
        """Skilar verði á aukatryggingu sem str"""
        return self.__extra_insurance_price[1]

    def set_small_car_price(self, new_price):
        """Tekur inn verð streng og breytir verðinu á smábíl"""
        self.__small_car_price[1] = new_price
    
    def set_sedan_price(self, new_price):
        """Tekur inn verð streng og breytir verðinu á fólksbíll"""
        self.__sedan_price[1] = new_price

    def set_five_seat_suv_price(self, new_price):
        """Tekur inn verð streng og breytir verðinu á fimm sæta jeppa"""
        self.__five_seat_suv_price[1] = new_price
    
    def set_seven_seat_suv_price(self, new_price):
        """Tekur inn verð streng og breytir verðinu á sjö sæta jeppa"""
        self.__seven_seat_suv_price[1] = new_price
    
    def set_minibus_price(self, new_price):
        """Tekur inn verð streng og breytir verðinu á smárútu"""
        self.__minibus_price[1] = new_price

    def set_base_insurance_price(self, new_price):
        """Tekur inn verð streng og breytir verðinu á grunntryggingu"""
        self.__base_insurance_price[1] = new_price

    def set_extra_insurance_price(self, new_price):
        """Tekur inn verð streng og breytir verðinu á aukatryggingu"""
        self.__extra_insurance_price[1] = new_price

    def read_car_prices(self):
        """Les uppúr price.csv og skilar lista af listum með nafni og verði"""
        the_list = []
        with open ("./data/price.csv", encoding = "UTF-8") as price_file:
            dict_reader_dicts = csv.DictReader(price_file)
            for row in dict_reader_dicts:
                the_list.append([row["car_type"],row["price"]])
        return the_list
    
    def update_price_list(self):
        """Skrifar inní price.csv, notar self.__price_list og prentar hann út línu fyrir línu(fyrsta línan er car_type,price"""
        with open ("./data/price.csv", "w", encoding = "UTF-8") as price_file:
            price_file.write("car_type,price\n")
            for price in self.__price_list:
                price_file.write(price[0] + "," + price[1] + "\n")
