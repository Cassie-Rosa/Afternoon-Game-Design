#Cassie Rosa
#calculating age 

import os 
os .system('cls')

born= int(input("year you were born: ")) #person can type year born in terminal
current= int(input("current year: ")) #person can type the current year

subtract= current - born 
print(subtract) #displays answer

if (subtract > 61):
    print (" your olddddd! heh")

if (subtract  < 60 ): #how do equal too
        print ("your a youngy")