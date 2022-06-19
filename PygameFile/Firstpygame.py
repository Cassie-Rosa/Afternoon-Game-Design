
# #Cassie Rosa
# #learning basic pygame functions 

#We are going to be learning how to control objects using keys
#We will also learn how to use images
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
# K_w                   w key
# K_a                   a key
# K_s                   s key
# K_d                   d key




import sys
from tkinter import W
import pygame, os, random, math
from datetime import datetime
import os, datetime
date=datetime.datetime.now()

pygame.init()

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')

WIDTH = 700#amount of pixels
HEIGHT = 700
colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")

#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game") # title of the window

#images
bg = pygame.image.load("PygameFile\images1\\bgSmaller.jpg")
char = pygame.image.load("PygameFile\images1\PixelArtTutorial.png")
char = pygame.transform.scale(char, (50,50))

char2=pygame.image.load ("PygameFile\Moving IMages\standing.png")
char2=pygame.transform.scale(char, (50,50))


#circle var

background = colors.get("grey")
cnt=0 




#this menu function it will be used to connect all of the functions to the buttons on the screen very important 
def menu():
    screen.fill(colors.get("white"))
    menu = TITLE_FONT.render("Circle Eats Square", 1, colors.get("black"))
    xd = WIDTH//2 - (menu.get_width()//2)
    screen.blit(menu, (xd, 100))\
    
    global ByTop 
    global ByBot
    global Bx1
    global Bx2
    global Bx3

    ByTop=HEIGHT//3
    ByBot=HEIGHT//2
    Bx1=WIDTH//9
    Bx2=Bx1*3.5
    # WIDTH//2-65
    Bx3=Bx2*1.73
    inst_button = pygame.Rect(Bx1, ByTop, 150, 50)
    setting_button = pygame.Rect(Bx2, ByTop, 150, 50)
    game1_button=pygame.Rect(Bx3,ByTop,150,50)
    game2_button=pygame.Rect(Bx1,ByBot,150,50)
    sb_button=pygame.Rect(Bx2,ByBot,150,50)
    exit_button=pygame.Rect(Bx3,ByBot,150,50)

    
    pygame.draw.rect(screen, colors.get("red"), inst_button)
    pygame.draw.rect(screen, colors.get("orange"), setting_button)
    pygame.draw.rect(screen, colors.get("yellow"), game1_button)
    pygame.draw.rect(screen, colors.get("green"), game2_button)
    pygame.draw.rect(screen, colors.get("blue"), sb_button)
    pygame.draw.rect(screen, colors.get("purple"), exit_button)

    #render
    text1 = MENU_FONT.render("Instructions", 1, colors.get("black"))
    text2 = MENU_FONT.render("Settings", 1, colors.get("black"))
    text3 = MENU_FONT.render("Game 1", 1, colors.get("black"))
    text4= MENU_FONT.render("Game 2", 1, colors.get("black"))
    text5 = MENU_FONT.render("Score Board", 1, colors.get("black"))
    text6 = MENU_FONT.render("Exit", 1, colors.get("black"))
   
    screen.blit(text1, (120, HEIGHT//3+10)) #
    screen.blit(text2, (320, HEIGHT//3+10))
    screen.blit(text3, (520, HEIGHT//3+10))
    screen.blit(text4, (120, HEIGHT//2+10))
    screen.blit(text5, (320, HEIGHT//2+10))
    screen.blit(text6, (520, HEIGHT//2+ 10)) 
    pygame.display.update()
    
    
    while True:
        # global Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False #this is not working 
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if inst_button.collidepoint(mx, my):
                    readfile("Instruction","PygameFile\Inst2.txt")
                    backB()
                if exit_button.collidepoint(mx,my):
                    exit()
                    pygame.quit()   
                    sys.quit()
                if sb_button.collidepoint(mx,my):
                    readfile("Score Board","PygameFile\FirstgameSB.txt")
                    backB()
                if setting_button.collidepoint(mx,my):
                    setting()
                    backB()
                if game1_button.collidepoint(mx,my):
                    game(char)
                    backB()
                if game2_button.collidepoint(mx,my):
                    game(char2)
                    backB()
                   

 # thisvis exit function this will pop up a a thank you screen and end game               
def exit():
    #This is where make a exit screen "thanks for playing"
    screen.fill(colors.get("white"))
    exitT = TITLE_FONT.render("Thank you for playing!", 1, colors.get("black"))
    xd = WIDTH//2 - (exitT.get_width()//2)
    screen.blit(exitT, (xd, 300))\
    #trying to make it delay and stay on screen for like 5 seconds and then closing 
    pygame.display.update()
    pygame.time.delay(1000)

    scrline=str(cnt)+"\t "+name +"\t" +date.strftime("%m / %d / %y")+ "\n "
    myFile=open("PygameFile\FirstgameSB.txt", 'a')
    myFile.write(scrline)
    myFile.close()
    
    # Game=False

# this will be the white background and use ADD to make easier so not repeate code 

#This is setting function that will give user option to change 
def setting():
    screen.fill(colors.get("white"))
    settingT= TITLE_FONT.render("Settings", 1, colors.get("black"))
    xd = WIDTH//2 - (settingT.get_width()//2)
    screen.blit(settingT, (xd, 50)) 

#this is button for choose the setting 
    Button_ss = pygame.Rect(WIDTH//18, HEIGHT//18, 80, 50)
    pygame.draw.rect(screen, colors.get("grey"), Button_ss)
    text1 = MENU_FONT.render("Back", 1, colors.get("white"))
    screen.blit(text1, (WIDTH//18+15, HEIGHT//18+10))
    
    pygame.display.update()



    # while True:
    #     global run 
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #             print("you quit")
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     mousePos = pygame.mouse.get_pos()
            #     mx = mousePos[0]
            #     my = mousePos[1]
            #     if .collidepoint(mx, my):
            #         return menu()
    #2 background options 



    
    



#This is both the scoreboard and the instruction pages able to use same function ****DONE
def readfile (title, fileName):
    screen.fill(colors.get("white"))
    scoreb = TITLE_FONT.render(title, 1, colors.get("black"))
    xd = WIDTH//2 - (scoreb.get_width()//2)
    screen.blit(scoreb, (xd, 50))\

    myFile = open(fileName, "r")
    content = myFile.readlines()

    #print the score 
    yi = 150
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
    
    
    

#This is a back button function so that I can call for it in all of the screens other than exit  *****DONE
def backB():
    Button_1 = pygame.Rect(WIDTH//18, HEIGHT//18, 80, 50)
    pygame.draw.rect(screen, colors.get("grey"), Button_1)
    text1 = MENU_FONT.render("Back", 1, colors.get("white"))
    screen.blit(text1, (WIDTH//18+15, HEIGHT//18+10))
    pygame.display.update()



    while True:
        global run 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint(mx, my):
                    return menu()
                
#functions
# menu()


#main Game
def game(charecter):
    cnt=0
    run=True
    cx = 350
    cy = 350
    rad = 25
    #square var
    hb = 50
    wb = 50
    xb = 325
    yb = 325
    square = pygame.Rect(xb,yb,wb,hb) #create the object to draw
    #char var
    charx = xb
    chary = yb
    #inscribed square
    ibox = rad*math.sqrt(2)
    xig = cx-(ibox/2)
    yig = cy-(ibox/2)
    insSquare=pygame.Rect(xig,yig,ibox,ibox)
    #bounce
    mountainSquare = pygame.Rect(250, 320, 180, 250)
    #Game Code
    speed = 2

    while run:
        # screen.fill(background)
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.blit(bg, (0,0)) #****************need to make this universal so I can use for both person and another shape
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() #allow us to see what key was pressed

        

        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            charx += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            chary += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            chary -= speed

        #circle and inscribed square movement
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed
        
        #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            cx = random.randint(rad, WIDTH-rad)
            cy = random.randint(rad, HEIGHT-rad)
            rad += 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
            cnt +=1 
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            charx = 10
            chary = 10
            cnt -=1
        
        #mountain collide circle
        if insSquare.colliderect(mountainSquare):
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, object)
        pygame.draw.rect(screen, colors.get("blue"), square)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        screen.blit(charecter, (charx, chary))

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
        
        pygame.display.update()
        pygame.time.delay(5)


#this is my call to the menu function which runs my whole game 
name =input("What is your name? ")
menu()






































