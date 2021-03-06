# Fiona Lee
# Write a program that outputs whether or not today is a weekday
# References: https://www.codespeedy.com/find-the-day-of-week-with-a-given-date-in-python/
# References: https://stackoverflow.com/questions/311627/how-to-print-a-date-in-a-regular-format

import datetime
Week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
# Defines weekdays as a list
today = datetime.datetime.today()
# Returns today's date in year, month, day & time
day = today.weekday()
# Returns position of the day of the week in number format 0-6

if day < 5:
   print()
   print("Today is", Week_days[day],"... Yes, Unfortunately today is a weekday.")
   #show day of the week with reference to position defined by 'day' in 'Week_days' list
else:
   print("Today is", Week_days[day],"... 'It's the weekend, yay!")