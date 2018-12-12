from models.Staff import Staff

class StaffRepository:
    '''þessi klasi vinur með að sækja allar uppl. um starfsmann og sendir þær í StaffService'''

    def __init__(self):      
        """Á eintak af lista sem inniheldur alla starfsmenn."""
        self.__staff = self.get_staff()
        
    
    def add_staff(self, staff):
        """Bæta starfsmanni eða yfirmanni í .csv skrá og í staff-listann."""
        with open("./data/staff.txt", "a", encoding = "UTF-8") as staff_file:
            staff_file.write(staff.__repr__() + '\n')
        self.__staff.append(staff)

    def get_staff(self):
        """Ná í alla starfsmenn úr skrá og skilar lista sem inniheldur þá alla."""
        staff_list = []
        with open("./data/staff.txt", encoding = "UTF-8") as staff_file:
            for row in staff_file.readlines():
                staff = eval(row.strip())
                staff_list.append(staff)
        return staff_list
    
    def update_staff_list(self):
        """Uppfærir skrá sem heldur utan um starfsmenn. Kallað er á þetta fall þegar
        lista sem inniheldur alla starfsmenn er breytt, þ.e. þegar starfsmanni er breytt.
        Skráin er þá uppfærð í takt við breytingarnar á listanum."""
        with open("./data/staff.txt", "w", encoding = "UTF-8") as staff_file:
            new_file = ""
            for staff in self.__staff:
                new_file += staff.__repr__() + "\n"
            staff_file.seek(0)
            staff_file.truncate()
            staff_file.write(new_file)

    def get_staff_list(self):
        """Skilar lista með öllum starfsmönnum."""
        return self.__staff