from models.Staff import Staff

class StaffRepository:

    def __init__(self):      
        self.__staff = self.get_staff()
    
    def add_staff(self, staff):
        """Bæta starfsmanni eða yfirmanni í .csv skrá og í stafalistann"""
        with open("./data/staff.csv", "a", encoding = "UTF-8") as staff_file:
            staff_file.write(staff.__repr__() + '\n')
        self.__staff.append(staff)

    def get_staff(self):
        """Ná í alla starfsmenn"""
        staff_list = []
        with open("./data/staff.csv", encoding = "UTF-8") as staff_file:
            for row in staff_file.readlines():
                staff = eval(row.strip())
                staff_list.append(staff)
        return staff_list

    def get_staff_list(self):
        return self.__staff