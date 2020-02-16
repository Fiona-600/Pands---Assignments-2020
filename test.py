
#Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#D = Wednesday

#today = datetime.datetime(2020, 2, 16)
#today.get_weekday()  
# what I look for

#for i = Wednesday

#print weekday()
    #print ("weekday")
#for j in range (6,7)
#print ("weekend")



import datetime

weekno = datetime.datetime.today().weekday()

if weekno<5:
    print ("Weekday")
else:
    print ("Weekend")

