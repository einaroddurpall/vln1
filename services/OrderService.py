from datetime import datetime, timedelta


class OrderService:

    def __init__(self):
        # self.__order_repo = OrderRepository
<<<<<<< HEAD
        pass
    
    def date_list(self, date1, date2):
        date_list = []
        date_to_list = date1
        while date1 <= date2:
            date_list.append(date_to_list)
            date_to_list += timedelta(days=1)
        return date_list

=======
>>>>>>> c5c6e863bdf11afdcf03dec29528cf60f81f3ef0
