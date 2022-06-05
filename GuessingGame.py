#Cassie Rosa
#guessing game
#doing a Disney princess guessing game
#physeodocode
#   start
#   input title
#   input instructions 


import os 
os .system('cls')
import random

#for i in range (100):                             |
for i in range (30): #makes > repeat 
    print(">", end ="")
print()

print("|  Guess the Disney Princess |")
print("|        instruction         |")  #The Title screen for the game 
print("|       instruction 2        |")

for i in range (30):
    print("<", end ="")
print()
#                                                  |

Disney=["Mickey Mouse", "", "kiwi", "papaya", "pear"] 

# for i in range (10): #this is a loop to repeat an action 10 times 
    # element=random.choice(myfruits) #this will choose a random fruit 
    # print(element)