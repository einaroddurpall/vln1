from repositories.StaffRepository import StaffRepository
from models.Employee import Employee
from models.Boss import Boss

class StaffService:

    def __init__(self):
        self.__staff_repo = StaffRepository()
        self.__staff_list = self.__staff_repo.get_staff_list()

    def check_login(self, username, password):
        for staff in self.__staff_list:
            if staff.get_username() == username and staff.get_password() == password:
                return True, staff.get_admin()
        return False, False