# Fiona Lee
# A function to find the square root of a given number

import math 
print()
n = float ( input ("Please enter a positive number: "))
# n is the base number supplied by the user i.e. 14.5
guess = float ( input ("Now guess of the square root of this number: "))
print () 
print ("Calculate the square root of" , round (n))
print()
print("First Guess is", round(guess))
# guess is the first approximate guess supplied by the user i.e. say 3
    
while (guess != math.sqrt (n)):
#Continue generating new guesses until the actual square root of n is reached:
    guess = ((guess + n/guess)/2)
    print ("Next Guess is" , round (guess , 20))
    #Show all guesses generated to 3 decimal places
    
else:
    print()
    print ("The square root of",n, "using Newton's Method is approximately", round (guess , 1))
    #Otherwise print result if guess equals the square root of n:

    
