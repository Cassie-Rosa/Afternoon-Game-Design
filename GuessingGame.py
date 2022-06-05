#Cassie Rosa
#guessing game
#doing a Disney princess guessing game
#physeodocode
#   start
#   input title
#   input instructions 
#   input 10 disney Princess into list
#   dicision pick a random princess
#   process give a hint for the chooses princess
#   process let player guess answer
#   dicision if guess correct input your correct 
#   dicision if guess incorrect input your wrong 
#           and input try again
#   process let player guess again 
#   dicision if guess correct input your correct 
#   dicision if guess incorrect input your wrong 
#           input game over 


import os 
os .system('cls')
import random

#for i in range (100):                             |
for i in range (36): #makes > repeat 
    print(">", end ="")
print()

print("|    Guess the Disney Princess!    |")
print("|  you get one hint with two trys  |")  #The Title screen for the game 
print("|         Made By: Cassie          |")

for i in range (36):
    print("<", end ="")
print()
#                                                  |

Disney=["Cinderella", "Belle", "Mulan", "Rapunzul", "Tiana","Arial","Snow white","Aurora","Jasmine", "Marida"] 

for i in range (1): #this is a loop to repeat an action 1 times 
    element=random.choice(Disney) #this will choose a random princess
    #print(element)

if element == "Cinderella": # this shows hint when a random word is selected 
    print("Hint: she has two wicked step-sister")

if element == "Belle":
    print("Hint: she falls for a beast")

if element == "Mulan":
    print("Hint: she has a pet cricket")

if element == "Rapunzul":
    print("Hint: she has long hair")

if element == "Tiana":
    print("Hint: she turns into a frog")

if element == "Arial":
    print("Hint: she has red hair")

if element == "Snow white":
    print("Hint: she has seven dwarfs")

if element == "Aurora":
    print("Hint: she sleeps for a longtime")

if element == "Jasmine":
    print("Hint: she rides a magic carpet")

if element == "Marida":
    print("Hint: she has a scottish accent")

guess=input("Enter a Disney Princess: ") # this makes so user can type answer in terminal 
if guess == element:
    print("WINNNNER! You did it") # if guess is correct then this messge pops up 
else:
    print("LOOOOSSERRRR! Your were incorrect") # if guess isnt answer then this messge pops up 

if guess != element: #if not right they are able to try again by doing the same code above but under the if statement
    print("try again!")

    guess2=input("Enter a Disney Princess: ")
    if guess2 == element:
     print("Finally! Your Correct")
    else:
     print("Not Again!! You Lost")

# if print("WINNNNER! You did it"):
#     input("play again? yes or no: ")   ----- I dont know how to make them be able to play again 



