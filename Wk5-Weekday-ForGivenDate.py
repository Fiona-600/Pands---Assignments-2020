# Fiona Lee

# Write a Python program to find day of the week for a given date 

import datetime
import calendar 

Week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
# Defines weekdays as a list

L = list (map (int (input("Enter today's date: "). split('/')))

day = datetime . date(L[2],L[1],L[0]). weekday()

if day < 5:

   print("Today is", Week_days[day],"... Yes, Unfortunately today is a weekday.")

else:
    
   print("Today is", Week_days[day],"... 'It's the weekend, yay!")