#Fiona Lee
#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
#Have the program end if the current value is one

print()
value = int (input ("Please Enter any Positive Integer: "))
print()
print ("Current Value is:", int (value))
#value = Current Value
print()
#Over-riding condition to execute only until a equals one
while value != 1:
    #Condition to be satisfied if Current Value is EVEN:
    if(value % 2) == 0:
        value / 2
        print("Current value is EVEN so successive value is", value ,"divided by 2 = ",int(value / 2))
    else:
        #Condition to be satisfied if Current Value is ODD:
        if(value % 2) != 0:
            ((value * 3) + 1)
            print("Current value is ODD so successive value is", value ,"multiplied by 3 plus one = ",int((value * 3) + 1))

    #Loop condition to create successive values:
    if (value % 2) == 0: 
        value = int(value / 2)
    else:
        value = int((value * 3) + 1)

