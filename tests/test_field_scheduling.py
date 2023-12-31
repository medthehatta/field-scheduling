import arrow

from field_scheduling import AvailabilityField

"""

weekday evenings
lunch except on thursdays
saturday mornings
all next week
not next wednesday but all following wednesdays


weekday & evening
lunch & ~thursdays
saturday & morning
next week
~(next week) & (subsequent (next week))


pad(day, ramp_up(5pm, 7pm) + flat(7pm, 8pm) + ramp_down(8pm, 9pm))

repeat(daily, bump(5pm, 7pm, 8pm, 9pm))
repeat(daily, ramp(5pm, 7pm))
repeat(daily, flat(7pm, 8pm))
"""


def test_reify_from_arrow():
    num_periods = 300
    start_ts = 1367900664
    start = arrow.get(start_ts)
    end = arrow.get(start_ts + 60*15*num_periods)
    expected = (start, [1]*(num_periods + 1))
    found = AvailabilityField.from_arrow_range(start, end).to_tuple()
    assert found == expected
