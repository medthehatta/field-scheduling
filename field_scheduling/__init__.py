"""field-scheduling - A library"""

__version__ = '0.1.0'
__author__ = 'Med Mahmoud <medthehatta@gmail.com>'
__all__ = []


from math import ceil

import arrow


hour_periods = 4
day_periods = 24 * hour_periods
week_periods = 7 * day_periods


class AvailabilityField:

    @classmethod
    def zeros(cls, periods):
        return cls([0]*(periods + 1))

    @classmethod
    def flat(cls, periods):
        return cls([1]*(periods + 1))

    @classmethod
    def ramp(cls, periods):
        return cls([n/periods for n in range(0, periods + 1)])

    @classmethod
    def from_arrow_range(cls, start, end):
        delta = end - start
        minutes = ceil(delta.total_seconds() / 60)
        periods = minutes // 15
        return cls([1]*(periods + 1), start)

    def __init__(self, field, start=None):
        self.start = start
        self.field = field

    def is_bound(self):
        return not self.is_unbound()

    def is_unbound(self):
        return self.start is None

    def to_tuple(self):
        return (self.start, self.field)
