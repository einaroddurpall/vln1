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

    def make_number(self, lenght_of_number, input_string, error_code_str):
        legal_ssn = False
        while not legal_ssn:
            inp = input(input_string)
            ssn = ""
            for letter in inp:
                try:
                    int(letter)
                    ssn += letter
                except:
                    print(error_code_str)
                    continue
            if len(ssn) == lenght_of_number:
                legal_ssn = True
            else:
                print(error_code_str)
        return ssn