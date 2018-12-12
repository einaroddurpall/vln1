from repositories.StaffRepository import StaffRepository
from models.Staff import Staff
from repositories.PriceRepository import PriceRepository

class StaffService:
    '''Þessi klasi vinnur úr öllum upplýsingum sem tengjast starfsmanni, skrá starfsmann, logga sig inn og 
    breyta uppl. sem tengjast honum'''

    def __init__(self):
        self.__staff_repo = StaffRepository()
        self.__staff_list = self.__staff_repo.get_staff_list()
        self.__price_repo = PriceRepository()

    def check_login(self, username, password):
        '''Gá hvort usernamið og passwordið sem slegið var inn stemmir'''
        for staff in self.__staff_list:
            if staff.get_username() == username and staff.get_password() == password:
                return True, staff.get_admin()
        return False, False

    def staff_register(self):
        '''Sendir skilaboð til reboið um add viðeigandi starfsmanni í skrána'''
        new_staff = Staff()
        new_staff = new_staff.make_staff(self.__staff_list)
        if type(new_staff) != str:
            self.__staff_repo.add_staff(new_staff)
            return new_staff
        else:
            return new_staff
    
    def staff_delete(self, staff):
        '''Eyðir starfsmanni úr listanum og sendir á repoið að eyða starfsmanni úr skránum'''
        self.__staff_list.remove(staff)
        self.__staff_repo.update_staff_list()

    def staff_update_info(self, staff):
        '''Updatear starfsmanns upplýsingar og sendir það á repoið að updata það'''
        staff.update_info(self.__staff_list)
        self.__staff_repo.update_staff_list()

    def check_ssn(self, ssn):
        '''Kíkir hvort viðeigandi kennitala stemmir og sendir þá starfsmannin sem á kennitöluna'''
        for staff in self.__staff_list:
            if staff.get_ssn() == ssn:
                return staff

    def change_price(self, choice):
        legal_price = False
        while not legal_price:
            new_price = input("Sláðu inn nýtt dagsverð: ")
            try:
                int(new_price)
                legal_price = True
            except:
                print("Það virkar einungis að slá inn tölur.")
                keep_going = input("1.  Reyna Aftur\nt.  Tilbaka\nh. Heim\n").lower()
                if keep_going == "t":
                    return False, False
                elif keep_going == "h":
                    return True, True
        if choice == "2":
            self.__price_repo.set_small_car_price(new_price)
        elif choice == "1":
            self.__price_repo.set_sedan_price(new_price)
        elif choice == "3":
            self.__price_repo.set_five_seat_suv_price(new_price)
        elif choice == "4":
            self.__price_repo.set_seven_seat_suv_price(new_price)
        elif choice == "5":
            self.__price_repo.set_minibus_price(new_price)
        self.__price_repo.update_price_list()
        return False, False
    
    def print_price_list(self):
        print("{:16} {:>10}\n".format("Flokkur","Verð"))
        for price_list in self.__price_repo.get_price_list():
            print("{:16} {:>10}".format(price_list[0], price_list[1]))
    