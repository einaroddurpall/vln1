class Person:
    """The person class takes in name and ssn 
    and is a parent class of costumer, Boss, and Employee"""

    def __init__ (self, name, ssn):
        self._name = name
        self._ssn = ssn

    def get_name(self):
        return self._name

    def get_ssn(self):
        return self._ssn

    def make_name(self):
        legal_name = False
        while not legal_name:
            name = input("Nafn: ")
            for letter in name:
                try:
                    int(letter)
                    print("Nafnið inniheldur ólöglega stafi")
                    legal_name = False
                    break
                except:
                    legal_name = True
        self._name = name