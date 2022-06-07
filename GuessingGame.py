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


Princess=["Cinderella", "Belle", "Mulan", "Rapunzul", "Tiana","Arial","Snow white","Aurora","Jasmine", "Marida"]
vilians=["Hades","Scar","Ursula", "Jafar","Gaston","Maleficent", "Cruella", "Evil Queen", "Captian Hook","Gothel"]
Animals=["Mushu","Louis", "Stitch", "Pumba","Abu","Timon","Zazu","Sebastian", "Flounder","Jiminy Cricket"]

count = 0 # ----------------------------------------
Game = True #----------------------------------

while Game:
    #for i in range (100):                             |
    for i in range (36): #makes > repeat 
        print(">", end ="")
    print()

    print("|      The Disney Guessing Game     |")

    for i in range (36): #makes > repeat 
        print("^", end ="")
    print()
    print("|  you get one hint with two trys  |")  #The Title screen for the game 
    print("|         Pick: 1) Princess        |")
    print("|         Pick: 2) Villians        |")
    print("|         Pick: 3) Sidekick        |")

    for i in range (36):
        print("<", end ="")
    print()
#                                                  |
    
   

    name= input("what is your name? ") # this will as them there name ------------
    print (name, end =", ") #-----------------------------------------
    answer= input("would you like to play The Disney Guessing Game? ") #-------------------------------
    answer=answer.lower() #----------------------------------------------
    if 'n' in answer: #------------------------------------------
        break # break will end or do game is false 
        
    while True:
        choice = input ("what game would you like to play? ")
        try:
            choice=int(choice)
            if choice > 0 and choice <4: # greater, lessthan
                 break
            else: 
                 print ("give me 1, 2, or 3")
        except:
            print("please enter a number")

    add = "" 
    if choice == 1:
        add= "princess"
        element=random.choice(Princess) #this will choose a random princess
       # Pguess= input("Guess a Disney Princess: ")
        print("You choose Princesses")
    #print(element)
    
    if choice== 2:
        add= "Villian"
        element=random.choice(vilians) 
       # Vguess=input("Guess a Disney Villian: ")
        print(" You choose Villians")

    if choice== 3:
        add="Sidekick"
        element=random.choice(Animals) 
       # Sguess=input("Guess the Disney Sidekick: ")
        print("You choose Sidekick")







#--------This was old hints but now different--------------------------------------------------------------------------------------------------
# if element == "Cinderella": # this shows hint when a random word is selected 
#     print("Hint: she has two wicked step-sister")

# if element == "Belle":
#     print("Hint: she falls for a beast")

# if element == "Mulan":
#     print("Hint: she has a pet cricket")

# if element == "Rapunzul":
#     print("Hint: she has long hair")

# if element == "Tiana":
#     print("Hint: she turns into a frog")

# if element == "Arial":
#     print("Hint: she has red hair")

# if element == "Snow white":
#     print("Hint: she has seven dwarfs")

# if element == "Aurora":
#     print("Hint: she sleeps for a longtime")

# if element == "Jasmine":
#     print("Hint: she rides a magic carpet")

# if element == "Marida":
#     print("Hint: she has a scottish accent")





    guess=input("Enter a Disney " + add + ": " ) # this makes so user can type answer in terminal 


    if guess == element:
        print("WINNNNER! You did it") # if guess is correct then this messge pops up 
    else:
        print("LOOOOSSERRRR! Your were incorrect") # if guess isnt answer then this messge pops up 

    if guess != element: #if not right they are able to try again by doing the same code above but under the if statement
        print("try again!")

        guess2=input("Enter a Disney "+ add + ": ")
        if guess2 == element:
            print("Finally! Your Correct")
        else:
            print("Not Again!! You Lost")
            print(element, "was the answer")

#------------------------------------
    for i in range (25): #makes > repeat 
        print(">", end ="")
    print()

    answer= input ("do you wanna play again? ")
    if ('n' or 'N') in answer: 
        print("Thank you for playing!!") 
        Game= False  

# if print("WINNNNER! You did it"):
#     input("play again? yes or no: ")   ----- I dont know how to make them be able to play again 



