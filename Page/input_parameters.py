import re


class Input_parameters():
    def __init__(self):
        self.Website = "https://www.trip.com/"
        self.Destination = "Beijing"
        self.Check_in_date = "18th Nov 2020"
        self.Night = 7
        self.Rooms = 1
        self.Adult = 2
        self.Children = 0

    def get_month(self):
        p = re.compile('\w+')
        month = (p.findall(self.Check_in_date)[1])
        return month

    def get_year(self):
        p = re.compile('\d+')
        year = int((p.findall(self.Check_in_date)[1]))
        return year

    def get_day(self):
        p = re.compile('\d+')
        day = (p.findall(self.Check_in_date)[0])
        return int(day)

    def get_to_date(self):
        to_date = self.get_day() + self.Night
        flag = 0
        while True:
            #print("get_to_date")
            if to_date > 28:
                to_date = to_date - self.get_day_of_month(self.get_month())
                flag = flag + 1
            else:
                break
        return [to_date, flag]

    def is_leap_year(self):
        year = self.get_year()
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def get_day_of_month(self, mon):
        d = {'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31, 'Jan': 31, 'Mar': 31,
             'Apr': 30, 'May': 31}
        if self.is_leap_year():
            d['Feb'] = 29
        else:
            d['Feb'] = 28
        return d[mon]
