from repositories.StaffRepository import StaffRepository
from models.Staff import Staff

class StaffService:

    def __init__(self):
        self.__staff_repo = StaffRepository()
        self.__staff_list = self.__staff_repo.get_staff_list()

    def check_login(self, username, password):
        for staff in self.__staff_list:
            if staff.get_username() == username and staff.get_password() == password:
                return True, staff.get_admin()
        return False, False

    def customer_register(self):
        new_staff = Staff()
        new_staff.make_staff(self.__staff_list)
        self.__staff_repo.add_staff(new_staff)
    
    def staff_delete(self, staff):
        self.__staff_list.remove(staff)
        self.__staff_repo.update_staff_list()

    def staff_update_info(self, staff):
        staff.staff_change_info(self.__staff_list)
        self.__staff_repo.update_staff_list()
        #Pæling með pantanir sem eru skráðar á gamla viðskiptavinin