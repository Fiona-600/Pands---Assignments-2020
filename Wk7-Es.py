# Fiona Lee

# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Text is sourced from https://web.archive.org/web/20050405224405/http://etext.lib.virginia.edu/etcbin/toccer-new2?id=Mel2Mob.sgm&images=images/modeng&data=/texts/english/modeng/parsed&tag=public&part=all

with open ("Moby-Dick.txt" , "r") as f:
      
    print("")
  
    frequency = (f.read () .lower (). count ('e'))
    
    print ("The number of times 'e' occurs in the book 'Moby Dick' is:" , frequency)
   
    
#Alternative Code:

#print ("")

#f = open ('Moby-Dick.txt','r')

#frequency = f.read() . lower () . count ('e')

#print ("The number of times 'e' occurs in the book 'Moby Dick' is:" , frequency)

#f.close ()