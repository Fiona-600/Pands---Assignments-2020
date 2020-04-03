# Fiona Lee
# A function to find the square root of a given number

import math 
a = float ( input ("Please enter a positive number: "))
while True:
    if a > 0:
        b = math.sqrt (a)
        print ("The square root of", a ,"is approx.", round ( b , 1))
    else:
        if a < 0:
        #If user tries to input a negative number in error
            print ("Error!! Number must be positive...please try again")
            a = float ( input ("Please enter a positive number: "))
            continue
    break

