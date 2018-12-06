from datetime import date
from models.Car import Car

class DateRepository:

    def __init__(self):
        """Á dictionary sem heldur utan um allar dagsetningar með bókunum. Dagsetningin er key og 
        value-in fyrir dagsetningarnar eru bílarnir sem eru bókaðir þann dag."""
        self.__dates_dict = self.get_date_dict()

    def add_car_to_date(self, date, car):
        """Tekur við bíl og dasetningu. Bætir bílnum við sem value í dictionary
        fyrir viðeigandi dagsetningar-key, ef dagsetningin er ekki til sem key
        er henni bætt við og bíllinn settur sem value. Þær upplýsingar eru svo
        skáðar í file sem geymir allar dagsetningar með bókunum og heldur utan
        hvaða bílar eru bókaðir þá dagsetningu."""
        if date in self.__dates_dict:
            self.__dates_dict[date].append(car)
            with open("./data/dates.csv", "r+", encoding = "UTF-8") as date_file:
                new_file = ""
                for line in date_file.readlines():
                    line_list = self.create_list(line)
                    the_date = self.create_date_from_string(line_list[0])
                    if the_date == date:
                        line_list.append(car.__repr__())
                    new_file += ";".join(line_list) + "\n"
                date_file.seek(0)
                date_file.truncate()
                date_file.write(new_file)
        else:
            self.__dates_dict[date] = [car]
            with open("./data/dates.csv", "a", encoding = "UTF-8") as date_file:
                new_line = str(date) + ";" + car.__repr__() + "\n"
                date_file.write(new_line)

    def get_date_dict(self):
        """Les skrána sem inniheldur bókaðar dagsetningar. Setur dagsetningarnar
        sem key í dictionary og setur alla bíla sem eru bókaðir á þeirri dagsetningu
        í lista og setur þann lista sem value fyrir viðeigandi dagsetningu."""
        date_dict = {}
        with open("./data/dates.csv", encoding = "UTF-8") as date_file:
            for line in date_file.readlines():
                line_list = self.create_list(line)
                the_date = self.create_date_from_string(line_list[0])
                for a_car in line_list[1::]:
                    if the_date in date_dict.keys(): 
                        date_dict[the_date].append(eval(a_car))
                    else:
                        date_dict[the_date] = [eval(a_car)]
        return date_dict

    def create_date_from_string(self, date_string):
        the_date_list = [int(i) for i in date_string.split("-")]
        the_date = date(the_date_list[0], the_date_list[1], the_date_list[2])
        return the_date

    def create_list(self, line_string):
        line_string = line_string.strip("\n")
        line_list = line_string.split(";")
        return line_list