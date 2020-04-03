#Fiona Lee
#Write a program that asks a user to input a string and outputs every second letter in reverse order

Sentence = input("Please Enter a Sentence:  ")
#User Input = "The quick brown fox jumps over the lazy dog..o zletrv pu o wr cu h"
#Output is every second letter of user input in reverse order
print ()
print("Your sentence in reverse order showing every second letter is: ",Sentence[:0:-2])
#This also works with print(Sentence[::-2])