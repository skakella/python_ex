#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
print(c.formatmonth(2021,2))

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# print(hc.formatmonth(2021,2))

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for d in c.itermonthdays4(2021,2):
#     print(d)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

year = 2021

print(calendar.monthcalendar(2021,5))
print(calendar.FRIDAY)

# for m in range(1,13):
#     firstWeek=
