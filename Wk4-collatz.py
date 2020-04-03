#Fiona Lee

#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
#Have the program end if the current value is one

print()
a = int(input("Please Enter any Positive Integer: "))
print()
print ("Current Value is:",int(a))
#a = Current Value
print()

#Over-riding condition to execute only until a equals one
while a != 1:
    
    #Condition to be satisfied if Current Value is EVEN:
    if(a % 2) == 0:
        a / 2
        print("Current value is EVEN so successive value is",a,"divided by 2 = ",int(a / 2))
    else:
        #Condition to be satisfied if Current Value is ODD:
        if(a % 2) != 0:
            ((a * 3) + 1)
            print("Current value is ODD so successive value is",a,"multiplied by 3 plus one = ",int((a * 3) + 1))

    #Loop condition to create successive values:
    if (a % 2) == 0: 
        a = int(a / 2)
    else:
        a = int((a * 3) + 1)

