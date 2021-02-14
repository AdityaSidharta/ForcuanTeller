from dateutil.relativedelta import relativedelta

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
