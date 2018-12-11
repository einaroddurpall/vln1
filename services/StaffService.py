from repositories.StaffRepository import StaffRepository
from models.Staff import Staff

class StaffService:
    '''þessi klasi vinnur úr öllum upplýsingum sem tengjast starfsmanni, skrá starfsmann, logga sig inn og 
    breyta uppl. sem tengjast honum'''

    def __init__(self):
        self.__staff_repo = StaffRepository()
        self.__staff_list = self.__staff_repo.get_staff_list()

    def check_login(self, username, password):
        '''Gá hvort usernamið og passwordið sem slegið var inn stemmir'''
        for staff in self.__staff_list:
            if staff.get_username() == username and staff.get_password() == password:
                return True, staff.get_admin()
        return False, False

    def staff_register(self):
        '''sendir skilaboð til reboið um add viðeigandi starfsmanni í skrána'''
        new_staff = Staff()
        legal = new_staff.make_staff(self.__staff_list)
        if legal == True:
            self.__staff_repo.add_staff(new_staff)
        else:
            pass
    
    def staff_delete(self, staff):
        '''eyðir starfsmanni úr listanum og sendir á repoið að eyða starfsmanni úr skránum'''
        self.__staff_list.remove(staff)
        self.__staff_repo.update_staff_list()

    def staff_update_info(self, staff):
        '''updatear starfsmanns upplýsingar og sendir það á repoið að updata það'''
        staff.update_info(self.__staff_list)
        self.__staff_repo.update_staff_list()

    def check_ssn(self, ssn):
        '''Kíkir hvort viðeigandi kennitala stemmir og sendir þá starfsmannin sem á kennitöluna'''
        for staff in self.__staff_list:
            if staff.get_ssn() == ssn:
                return staff
