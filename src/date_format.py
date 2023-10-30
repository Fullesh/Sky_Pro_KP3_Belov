import datetime as dt


def format_date(date):
    date_time_obj = dt.datetime.strptime(date[:10], '%Y-%m-%d')
    result_date = dt.datetime.strftime(date_time_obj, '%d.%m.%Y')
    return result_date
