from os import system,name
from services.StaffService import StaffService
from time import sleep
from models.methods import print_header, error_handle
from models.Staff import Staff

class StaffMenu:

    def __init__(self):
        self.__staff_service = StaffService()
        self.staff_menu()

    def staff_menu(self):
        """her er hægt að skrá nýjan aðgan að forritinu"""
        done = False
        while not done:
            prompt = "Heimasíða / Starfsmenn"
            print_header(prompt)
            action = input("1.  Skrá nýjan starfsmann\n2.  Leita af starfsmanni\n3.  Heim\n")
            if action == "1":
                prompt += " / Skrá nýjan starfsmann"
                print_header(prompt)
                self.__staff_service.staff_register()
            elif action == "2":
                exit_info = ""
                while exit_info == "":
                    if  "/ Leita að starfsmanni" not in prompt:
                        prompt += " / Leita að starfsmanni"
                    print_header(prompt)
                    ssn = input("Kennitala: ")
                    staff = self.__staff_service.check_ssn(ssn)
                    exit_info2 = ""
                    if staff:
                        while exit_info2 == "":
                            prompt = "Heimasíða / Starfsmenn / Leita að starfsmanni"
                            print_header(prompt)
                            print(staff)
                            choice = input("1.  Breyta upplýsingum starfsmann\n2.  Afskrá starfsmann\n3.  Tilbaka\n4.  Heim\n")
                            if choice == "1":
                                prompt += " / Breyta upplýsingum starfsmann"
                                print_header(prompt)
                                self.__staff_service.staff_update_info(staff)
                            elif choice == "2":
                                prompt += " / Afskrá starfsmann"
                                print_header(prompt)
                                choice = input("Ertu viss?(j/n): ")
                                if choice == "j":
                                    self.__staff_service.staff_delete(staff)
                                    exit_info = "Tilbaka"
                                    exit_info2 = "Tilbaka"
                            elif choice == "3":
                                exit_info = "Tilbaka"
                                exit_info2 = "Tilbaka"
                            else:
                                exit_info = "Heim"
                                exit_info2 = "Heim"
                                done = True
                    else:
                        choice = input('Kennitalan: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\n2.  Tilbaka\n3.  Heim\n'.format(ssn))
                        if choice == "2":
                            exit_info = "Tilbaka"
                        elif choice == "3":
                            exit_info = "Heim"
                            done = True
            else:
                done = True
