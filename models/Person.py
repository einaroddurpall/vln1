

class Person:
    """The person class takes in name and ssn 
    and is a parent class of costumer, Boss, and  Employee"""

    def __init__ (self, name, ssn):
        self.__name = name
        self.__ssn = ssn

    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__name



