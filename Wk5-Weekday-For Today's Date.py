# Fiona Lee

# Write a program that outputs whether or not today is a weekday

import datetime

Week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
# Defines weekdays as a list

now = datetime.datetime.now()
# Returns date in year, month day, hour, min, second, milisecond

day = now.weekday()
# Returns position of the day of the week in number format 0-6

if day < 5:

   print("Today is", Week_days[day],"... Yes, Unfortunately today is a weekday.")
   #show day of the week with reference to position defined by 'day' in 'Week_days' list

else:
    
   print("Today is", Week_days[day],"... 'It's the weekend, yay!")