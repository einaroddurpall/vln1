from datetime import date, timedelta
from os import system
from time import sleep
import string

def print_header(prompt=""):
        """ Hreinsar terminal og prentar út header með slóð """
        system('clear')
        print(prompt)
        print("="*70)

def make_date(a_date):
    """Tekur við dagsetningu í formi strengs og skilar date-tilviki fyrir þann dag."""
    new_string = ""
    for letter in a_date:
        if letter in string.digits:
            new_string += letter
    day = new_string[:2]
    month = new_string[2:4]
    year = new_string[4:]
    return date(int(year), int(month), int(day))

def make_car_type():
    '''spyr notandann um hvaða flokk af bíl hann vill fá og skilar síðan bílnumsem hann vill fá í streng'''
    valid_car_types = ["Fólksbíll", "Smábíll","Fimm sæta jeppi","Sjö sæta jeppi","Smárúta"]
    valid_car_type = False
    while valid_car_type is False:
        number = input("Flokkur bíls: \n1.  Fólksbíll\n2.  Smábíll\n3.  Fimm sæta jeppi\n4.  Sjö sæta jeppi\n5.  Smárúta\n")
        try:
            number = int(number)
            car_type = valid_car_types[number -1]
            return car_type
        except:
            print("Númerið: {} er ekki í listanum, reyndu aftur.".format(number))
            # if number.lower() == 'h' or number.lower() == 't':
            #     return None

def error_handle(search, search_input):
    '''sendir error á skjáin hjá notandanum ef hann gerir einhverja villu'''
    choice = input('{}: "{}" fannst ekki í kerfinu.\n1.  Reyna aftur\nt.  Tilbaka\nh.  Heim\n'.format(search, search_input))
    return choice.lower()

def make_number(lenght_of_number, input_string, error_code_str):
    '''þegar notandinn slær inn kennitölu eða símanumer checkar þetta fall hvort það sér rétt langt og hvort allir stafir 
    sér int annars sendir villu boða og biður um notanda að slá inn aftur'''
    legal_number = False
    while not legal_number:
        inp = input(input_string).lower()
        if inp == "h" or inp == "t":
            return inp
        number = ""
        for letter in inp:
            try:
                int(letter)
                number += letter
            except:
                number = ""
                break
        if len(number) == lenght_of_number:
            legal_number = True
        else:
            print(error_code_str)
    return number
    
def check_registration_num(registration_num):
    """Þetta fall tekur inn numeraplötu sem notandi sló inn og checkar hvort hún sé í lagi"""
    new_registration_num = ""
    for letter in registration_num:
        if (letter in string.ascii_letters) or (letter in string.digits):
            new_registration_num += letter
    if len(new_registration_num) != 5:
        print("Þetta bílnúmer var ólöglegt.")
        sleep(1)
        return False
    registration_num = new_registration_num.upper()
    # Ef bílnúmerið er löglegt þá er skilað bílnumerinu, bara verið að cheacka alla möglega innslætti.
    if registration_num[0] in string.ascii_letters and registration_num[1] in string.ascii_letters\
    and (registration_num[2] in string.ascii_uppercase or registration_num[2] in string.digits)\
    and registration_num[3] in string.digits and registration_num[4] in string.digits:
        return registration_num
    print("Þetta bílnúmer var ólöglegt.")
    sleep(1)
    return False

def make_date_list(date1, date2):
    """Tekur við tveimur dagsetningum og skilar lista með öllum dögum á milli þeirra ásamt endadögunum tveimur."""
    date_list = []
    date_to_list = date1
    while date_to_list <= date2:
        date_list.append(date_to_list)
        date_to_list += timedelta(days=1)
    return date_list

def pretty_str(number, unit):
    '''þetta fall tekur inn tölu, og einingu og setur punkta inn á milli þriðja hvern staf og eininguna á aftast 
    og skilar því sem streng'''
    number_str = str(number)
    number_new_str = ""
    for index, letter in enumerate(number_str[::-1]):
        if index % 3 == 0 and index != 0:
            number_new_str += "."
        number_new_str += letter
    return number_new_str[::-1] + " " + unit

def legal_dates(prompt):
    '''biður notanda um að slá inn dagsetningar og passar að þær séu rétt slegnar inn'''
    valid_dates = False
    while not valid_dates:
        try:
            date1 = make_date(input("Afhendingardagur (DD.MM.YYYY): "))
            if date1 < date.today():
                print("Villa: Þú getur ekki skoðað/pantað bíla aftur í tímann, vinsamlegast sláðu inn gilda dagsetningu.")
                input('Ýttu á "Enter" til að reyna aftur')
                print_header(prompt)
            else:
                date2 = make_date(input("Skiladagur (DD.MM.YYYY): "))
                if date1 <= date2:
                    valid_dates = True
                else:
                    print("Villa: Afhendingardagur getur ekki verið á undan skiladegi, vinsamlegast sláðu inn gilda dagsetningu.")
                    input('Ýttu á "Enter" til að reyna aftur')
                    print_header(prompt)
        except: 
            print("Villa: Dagsetning ekki til, vinsamlegast sláðu inn gilda dagsetningu.")
            input('Ýttu á "Enter" til að reyna aftur')
            print_header(prompt)
    return date1, date2

def pretty_date (date):
    '''Þetta fall tekur dagsetningu og skilar henni í betra formi'''
    return date[8:10] + "/" + date[5:7] + "/" + date[0:4]

def take_payment(price, price_promt="Verð"):
    '''Þetta fall spyr notandann hvort hann vilji borga, og hvernig, ef hann hættir við skráist ekki pöntun inn í kerfið'''
    payment_complete = False
    while not payment_complete:
        print("{}: {}".format(price_promt, pretty_str(price, "ISK")))
        pay_choice = input("1.  Borga með korti\n2.  Borga með reiðufé\nh.  Hætta við\n").lower()
        if pay_choice == "h":
            return "h"
        # EF notandi vill borga með pening er sent yfir í take_cash fallið
        elif pay_choice == "2":
            complete = take_cash(price)
            if type(complete) != bool:
                if complete == "h":
                    return "h"
            else:
                payment_complete = True
        elif pay_choice == "1":
            payment_complete = True
    return True

def take_cash(price):
    '''Þetta fall reiknar ef notandi kýs að borga með pening, reiknar afgnag þess og gáir hvort upphæð notanda stemmir
    sendir hann í gengum nokkur skref ef hún gerir það ekki'''
    legal_amount = False
    while not legal_amount:
        amount = input("Sláðu inn magn (ISK): ")
        try:
            amount = int(amount)
        except:
            print("Sláðu einungis inn tölustafi.")
            keep_going = input("1.  Reyna aftur\nt.  Tilbaka\nh.  Hætta við\n").lower()
            if keep_going == "t":
                return "t"
            elif keep_going == "h":
                return "h"
        if amount >= price:
            print("Greiðsla tókst: Afgangur er {} ISK".format(amount - price))
            input('Ýttu á "Enter" til að halda áfram.')
            return True
        # Ef greiðsla nægir ekki spyr kerfið hvort hann vilji borga með kort rest eða pening eða hætta við
        else:
            final_pay_choice = input("Greiðsla nægir ekki, {} ISK vantar uppá\n1.  Borga restina með korti á skrá\n2.  Borga restina með pening\nh. hætta\n".format(pretty_str(price - amount, "ISK"))).lower()
            if final_pay_choice == "h":
                return "h"
            elif final_pay_choice == "2":
                price -= amount
                print("\nVerð: {}".format(pretty_str(price, "ISK")))
                continue
            else:
                return True

def calc_price(order, price_repo):
    """Calculates the price of an order"""
    car = order.get_car()
    car_type = car.get_car_type()
    base_price = get_car_price(car_type, price_repo)
    dates = len(order.get_date_list())
    insurance = order.get_insurance()
    if insurance == 'Grunntrygging':
        insurance_price = int(price_repo.get_base_insurance_price())
    else:
        insurance_price = int(price_repo.get_extra_insurance_price())
    return (dates)*(base_price + insurance_price)

def get_car_price(car_type, price_repo):
    '''Tekur inn streng sem lýsir bíltegundinni og skilar verðið á þeim flokki'''
    if car_type.lower() == "smábíll":
        return int(price_repo.get_small_car_price())
    elif car_type.lower() == 'fólksbíll':
        return int(price_repo.get_sedan_price())
    elif car_type.lower() == 'fimm sæta jeppi':
        return int(price_repo.get_five_seat_suv_price())
    elif car_type.lower() == 'sjö sæta jeppi':
        return int(price_repo.get_seven_seat_suv_price())
    elif car_type.lower() == 'smárúta':
        return int(price_repo.get_minibus_price())
