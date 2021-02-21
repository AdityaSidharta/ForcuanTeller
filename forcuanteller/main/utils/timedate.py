import datetime

from dateutil.relativedelta import relativedelta

def validate_datetime(date_string, format_date):
    """Validating the date_string given to have the exact date format"""
    try:
        datetime.datetime.strptime(date_string, format_date)
    except ValueError:
        raise ValueError("Incorrect data format : {}, should be {}".format(date_string, format_date))



def get_period(period):
    number = period[:-1]
    unit = period[-1]

    assert unit in ["d", "h", "m", "s"]
    assert number.isdigit()
    return period


def get_interval(interval):
    number = interval[:-1]
    unit = interval[-1]

    assert unit in ["d", "h", "m", "s"]
    assert number.isdigit()
    return interval
