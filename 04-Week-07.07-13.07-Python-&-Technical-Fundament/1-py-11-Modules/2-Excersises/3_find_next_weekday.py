import calendar
import datetime


def find_next_weekday(start_date_str, target_weekday_name):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    target_weekday_number = list(calendar.day_name).index(target_weekday_name)
    start_weekday_number = start_date.weekday()
    days_ahead = (target_weekday_number - start_weekday_number + 7) % 7
    if days_ahead == 0:
        days_ahead = 7
    next_date = start_date + datetime.timedelta(days=days_ahead)
    return next_date.strftime("%Y-%m-%d")
