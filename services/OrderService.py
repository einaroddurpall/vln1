from datetime import datetime, timedelta


class OrderService:

    def __init__(self):
        # self.__order_repo = OrderRepository
        pass
    
    def date_list(self, date1, date2):
        date_list = []
        date_to_list = date1
        while date1 <= date2:
            date_list.append(date_to_list)
            date_to_list += timedelta(days=1)
        return date_list

