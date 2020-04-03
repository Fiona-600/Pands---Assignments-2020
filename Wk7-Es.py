# Fiona Lee

# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Text is sourced from https://web.archive.org/web/20050405224405/http://etext.lib.virginia.edu/etcbin/toccer-new2?id=Mel2Mob.sgm&images=images/modeng&data=/texts/english/modeng/parsed&tag=public&part=all

with open ("Moby-Dick.txt" , "r") as f:
# Open text file called 'Moby-Dick.text file in read mode
   
   print("")
   frequency = (f.read () .lower (). count ('e'))
   # Read all characters in the file, convert to lower case and count 
   # the number of times 'e' appears

   print ("The number of times 'e' occurs in the book 'Moby Dick' is:" , frequency)
   # Print the result
