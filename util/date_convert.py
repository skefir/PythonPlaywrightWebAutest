from dateutil import parser
from datetime import datetime, date, timedelta, time

from dateutil.relativedelta import relativedelta

DATE_FORMAT = '-d %b %Y'
DATE_TIME_FORMAT = 'd MMM yyyy %H:%M O'
MIDNIGHT_TIME = time(0, 0, 0)


def convert_str_to_datetime(date_string: str) -> datetime:
    return _date_parse(date_string)


def _date_parse(date_string: str) -> date|datetime:
    try:
        # dateutil.parser.parse() автоматически разбирает сложные форматы
        dt_object = parser.parse(date_string)
        return dt_object
    except ValueError as e:
        print(f"Ошибка при разборе даты '{date_string}': {e}")
        return None


def convert_str_to_date(date_string: str) -> date:
    return _date_parse(date_string)

def first_day_of_month(target_date: date) -> date:
    return target_date.replace(day=1)

def last_day_of_month(target_date: date) -> date:
    return target_date.replace(day=1) + relativedelta(months=1) - timedelta(days=1)