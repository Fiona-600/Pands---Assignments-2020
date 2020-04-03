# Fiona Lee
# A function to find the square root of a given number

import math 
value = float ( input ("Please enter a positive number: "))
while True:
    if value > 0:
        squareroot = math.sqrt (value)
        print ("The square root of", value ,"is approx.", round ( squareroot , 1))
    else:
        if value < 0:
        #If user tries to input a negative number in error
            print ("Error!! Number must be positive...please try again")
            value = float ( input ("Please enter a positive number: "))
            continue
    break

