class Person:
    """The person class takes in name and ssn 
    and is a parent class of costumer, Boss, and  Employee"""

    def __init__ (self, name, ssn):
        self.name = name
        self.ssn = ssn

    def get_name(self):
        return self.name

    def get_ssn(self):
        return self.name



