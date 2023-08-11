"""field-scheduling - A library"""

__version__ = '0.1.0'
__author__ = 'Med Mahmoud <medthehatta@gmail.com>'
__all__ = []


from math import ceil

import arrow


hour_periods = 4
day_periods = 24 * hour_periods
week_periods = 7 * day_periods


def zeros(periods):
    return [0]*(periods + 1)


def flat(periods):
    return [1]*(periods + 1)


def ramp(periods):
    return [n/periods for n in range(0, periods + 1)]


def reify(start, field):
    return (start, field)


def reify_from_arrow(start, end):
    delta = end - start
    minutes = ceil(delta.total_seconds() / 60)
    periods = minutes // 15
    return (start, [1]*(periods + 1))
    
