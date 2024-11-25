import calendar
from datetime import datetime

def get_month_calendar(year, month):
    return calendar.month(year, month)

def is_leap_year(year):
    return calendar.isleap(year)

def get_day_of_week(year, month, day):
    weekday = calendar.weekday(year, month, day)
    return calendar.day_name[weekday]

def days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

def current_date_info():
    today = datetime.now()
    return {
        "year": today.year,
        "month": today.month,
        "day": today.day,
        "weekday": calendar.day_name[today.weekday()]
    }