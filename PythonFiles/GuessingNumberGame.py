#Cassie Rosa
#Guessing Number Game
#using functions
#using files
#using strings
# showing a score board

#random.randint(1, 25)

import os 
os .system('cls')
import random

guess= 0
thenumb=0
#Hint 
def hint(guess, thenumb):
       #allow us to modify the variable all over the program
    # if cnt ==0:
    if (guess > thenumb):
        print ("not quite, too high")
    if (guess < thenumb):
        print ("not quite, too low")
        
Game = True
cnt = 0 
high=0
#Main Menu
def menu():
    for i in range (30): #makes > repeat 
        print(">", end ="")
    print()

    print("|     Guess The Number!      |")

    for i in range (30): #makes > repeat 
            print("<", end ="")
    print()

    print("|      Instructions---0      |")  #The Title screen for the game 
    print("|        Level 1------1      |")
    print("|        Level 2------2      |")
    print("|        Level 3------3      |")
    print("|       Score & Exit--4      |")

    for i in range (30): #makes > repeat 
            print("^", end ="")
    print()
    

#Main Game Loop
choice=0

def selectnum(choice):  #is a function with a parameter
    global thenumb
    global scrline
    if choice == 0:
        myfile= open("Instr.txt","r") 
        stuff=myfile.readlines()
        myfile.close()
        for line in stuff:
           print(line)
        input("press enter to go back to main menu")
    if choice ==1:
        # add= '"1-25" -------------------------
        thenumb= random.randint(1, 25)    
    if choice ==2:
        # add= "1-50"----------------------------
        thenumb= random.randint(1, 50)
    if choice ==3:
        # add= "1-100"----------------------------
        thenumb= random.randint(1, 100)
    if choice== 4:
        scrline=name+"\t"+str(cnt)+"\n " 
    return thenumb
        #go to score board and exit 




name =input("What is your name? ")
high=0 #to find highest score


while Game:
    menu()
    print(name, end=", ")
    
    while True:
        choice=input("input a menu number, ")
        #preventing error we use try and except
        try:
            choice=int(choice)
            if choice>=0 and choice <5:
                break
            else:
                print("give me 0, 1, 2, 3, or 4")
        except:
            print("sorry")
    print(choice)
    selectnum(choice)


    thenumb = selectnum(choice) #call to a function that will return a value
    #call function to select the word from the right list
    os.system('cls')
    check=True
    while check and choice != 0 and choice != 4:
        guess=int(input("Enter your a number: "))
        print()
        if guess == thenumb:
            print("Congrats, You got it")
            check=False
        else:
            hint(guess, thenumb)
        cnt+=1   # cnt= cnt + 1
        


    if choice != 0 and choice != 4:
        if cnt > high:   # find highest sce
            high=cnt
        print(name+", your score is "+str(cnt))
        input("Press enter ")
        os.system('cls')
        print("<><><><><><><><><><><><>")
        answer=input("Do yo want to play again? ")
        if ('n' or 'N') in answer:
            Game=False
            print("Thank you for playing!" )
            input("press enter to see your score")
    
    # cnt=0 
print("your highest score is " + str(high))


scrline=name+"\t"+str(cnt)+"\n " 
myFile=open("trysc.txt", 'a')
myFile.write(scrline)
myFile.close()
myFile=open("trysc.txt", 'r')
stuff= myFile.readlines()
myFile.close()
for line in stuff:
    print(line)
