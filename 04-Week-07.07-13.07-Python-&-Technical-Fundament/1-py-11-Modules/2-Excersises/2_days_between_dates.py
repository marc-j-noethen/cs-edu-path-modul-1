from datetime import datetime


def days_between_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d").date()
        date2 = datetime.strptime(date_str2, "%Y-%m-%d").date()
        return abs((date2 - date1).days)
    except ValueError:
        return None
