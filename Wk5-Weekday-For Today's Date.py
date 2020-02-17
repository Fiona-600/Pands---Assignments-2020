# Fiona Lee

# Write a program that outputs whether or not today is a weekday
# Python program to Find day of the week for a given date 

import datetime

Week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

now = datetime.datetime.now()
day = now.weekday()

if day < 5:

   print("Today is", Week_days[day],"... Yes, Unfortunately today is a weekday.")

else:
    
   print("Today is", Week_days[day],"... 'It's the weekend, yay!")