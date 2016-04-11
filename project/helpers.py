import datetime


# date conversion
def date_time_standard(date):
    date = datetime.datetime.strftime(date, '%d.%m.%Y %H:%M:%S')
    return date