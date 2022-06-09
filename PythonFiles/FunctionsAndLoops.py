# Cassie Rosa 
# from ctypes.wintypes import WORD
# This is not my code--- Fernando's
# 



import random
import os 

os.system ('cls')
from time import sleep
seconds=.5


list = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
theword=random.choice(list)

count = 0 # ----------------------------------------
Game = True #----------------------------------------------------------------

def hint(): #
    global count #-----------------------------------------------------
    if count == 0: #-----------------------------------------------------
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
           #-------------------------------------------------
    elif count ==1: #-----------------------------------------------------
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")
#hint() ------ this will run the function --------------------------------

while Game: # confused supposed to be blue----------------------------------
        
    
    print("|***************************************|")
    print("|         Guess The Animal!!!           |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|          1.Instructions               |")
    print("|   1. animals 2.fruits 3.computer parts|")
    print("|     You must guess one of them        |")
    print("|First we will provide you with one hint|")
    print("|           !Your Hint Is!              |")
    print("|  These animals are big fans of water  |")
    print("|***************************************|")

    theword=random.choice(list) # put here instead so new word each time --------------------


    name= input("what is your name?") # this will as them there name ------------
    print (name, end =",") #-----------------------------------------
    answer= input("would you like to play the game?") #-------------------------------
    answer=answer.lower() #----------------------------------------------
    if 'n' in answer: #------------------------------------------
        break # break will end or do game is false 
    
    while True:
        choice = input ("what game would you like to play?")
        try:
            choice=int(choice)
            if choice > 0 and choice <4: # greater, lessthan
                break
            else: 
                print ("give me 1, 2, or 3")
        except:
            print("please enter a number")


    os.system('cls') #-------------------------------------------------------
    check = True #--------------------------------------------------------
    while check and count < 5: #----------------------------------------------


        guess=input("plese put your guess here: ") 
        if guess == theword:#-------------------------------------------------
            print("Congrats, You got it") 
            check = False #------------------------------------
        else:
            hint()#------------------------------------
        count += 1#------------------------------------
    os.system('cls')#------------------------------------
    answer= input (" do you wanna play again")
    if ('n' or 'N') in answer:
        Game= False 
        Print ("Thanks you for playing")   









# guess2 = input("plese put your new guess here: ")
# if guess2 == theword:
#     print("Congrats, You got it")
# else:
#     print("wrong again, you are pretty bad at this, try again")


# guess3 = input("plese put your final guess here: ")

# if guess3 == theword:
#     print("Congrats, You got it")
# else:
#     print("You are horrible at guessing, no more hints, go till you get it right")

# while True:
#     ans = input("plese put your guess here: ")
#     if ans == theword:
#         name = True 
#         print("Congrats, You got it")
#         break 
#     else:
#         print("wrong again, try again")

