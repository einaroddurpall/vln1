from models.Person import Person

class Boss(Person):
    """Boss class, is a subclass of the Person class
    takes in name, ssn. 
    and the name and ssn get's sent to person parent class"""

    def __init__ (self, name = "", ssn = "", username = "", password = ""):
        Person.__init__(self, name, ssn)
        self.__username = username
        self.__password = password
        self.__admin = True

    def __repr__(self):
        return "Boss('{}','{}','{}','{}',{})".format(
            self._name, self._ssn, self.__username, self.__password, self.__admin
        )

    def __str__(self):
        return "Nafn: {}\nKennitala: {}\nNotandanafn {}\nLykilorð {}\nAðgengi {}".format(
            self._name, self._ssn, self.__username, self.__password, self.__admin
        )
    
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_admin(self):
        return self.__admin

