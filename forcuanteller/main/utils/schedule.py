import schedule

from forcuanteller.main.utils.timedate import validate_datetime


def get_scheduler(sched):
    assert isinstance(sched, tuple)
    assert len(sched) == 2
    date, time = sched
    validate_datetime(time, "%H:%M")

    if date == 'day':
        schedule.every().day.at(time)
    elif date == 'monday':
        schedule.every().monday.at(time)
    elif date == 'tuesday':
        schedule.every().tuesday.at(time)
    elif date == 'wednesday':
        schedule.every().wednesday.at(time)
    elif date == 'thursday':
        schedule.every().thursday.at(time)
    elif date == 'friday':
        schedule.every().friday.at(time)

    raise NotImplementedError("{}, {} is not implemented".format(date, time))
