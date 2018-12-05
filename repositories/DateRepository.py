from datetime import date
from models.Car import Car

class DateRepository:

    def __init__(self):
        self.__dates_dict = self.get_date_dict()

    def add_car_to_date(self, date, car):
            if date in self.__dates_dict:
                self.__dates_dict[date].append(car)
                with open("./data/dates.csv", "r+") as date_file:
                    new_file = ""
                    for line in date_file.readlines():
                        line = line.strip("\n")
                        line = line.split(";")
                        the_date = self.create_date_from_string(line[0])
                        if the_date == date:
                            line.append(car.__repr__())
                        new_file += ";".join(line) + "\n"
                    date_file.seek(0)
                    date_file.truncate()
                    date_file.write(new_file)
            else:
                self.__dates_dict[date] = [car]
                with open("./data/dates.csv", "a") as date_file:
                    new_line = str(date) + ";" + car.__repr__() + "\n"
                    date_file.write(new_line)

    def get_date_dict(self):
        date_dict = {}
        with open("./data/dates.csv") as date_file:
            for line in date_file.readlines():
                line = line.strip("\n")
                line = line.split(";")
                the_date = self.create_date_from_string(line[0])
                for a_car in line[1::]:
                    if the_date in date_dict.keys(): #date_dict[the_date]:
                        date_dict[the_date].append(eval(a_car))
                    else:
                        date_dict[the_date] = [eval(a_car)]
        return date_dict

    def create_date_from_string(self, date_string):
        the_date_list = [int(i) for i in date_string.split("-")]
        the_date = date(the_date_list[0], the_date_list[1], the_date_list[2])
        return the_date
