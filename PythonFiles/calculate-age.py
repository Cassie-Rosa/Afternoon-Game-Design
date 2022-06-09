#Cassie Rosa
#calculating age 

import os 
os .system('cls')

born= int(input("year you were born: ")) #person can type year born in terminal
current= int(input("current year: ")) #person can type the current year

subtract= current - born 
print(subtract) #displays answer

if (subtract > 51 and subtract == 51):
    print (" your olddddd")

if (subtract  < 50 and subtract == 50): #how do equal too
    print ("your young")