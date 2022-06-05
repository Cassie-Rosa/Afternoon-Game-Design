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

for i in range (1): #this is a loop to repeat an action 10 times 
    element=random.choice(Disney) #this will choose a random fruit 
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

guess=input("Enter a Disney Princess: ") 
if guess == element:
    print("WINNNNER! You did it") 
else:
    print("LOOOOSSERRRR! Your were incorrect")

if guess != element:
    print("try again!")

    guess2=input("Enter a Disney Princess: ")
    if guess2 == element:
     print("Finally! Your Correct")
    else:
     print("Not Again!! You Lost")

# if print("WINNNNER! You did it"):
#     input("play again? yes or no: ")



