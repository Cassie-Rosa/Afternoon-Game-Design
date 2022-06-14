# # # #Cassie Rosa
# # # #learning basic pygame functions 

# # #We are going to be learning how to control objects using keys
# # #We will also learn how to use images
# # # K_UP                  up arrow
# # # K_DOWN                down arrow
# # # K_RIGHT               right arrow
# # # K_LEFT                left arrow
# # # K_w                   w key
# # # K_a                   a key
# # # K_s                   s key
# # # K_d                   d key



# from cgitb import text
# from locale import CHAR_MAX
# from re import T
# from tkinter import Menu
# import pygame, os, time, random, math
# pygame.init()

# # print(pygame.font.get_fonts())
# # pygame.time.delay(10000)
# TITLE_FONT = pygame.font.SysFont('comicsans', 40)
# MENU_FONT = pygame.font.SysFont('comicsans', 20)

# os.system('cls')

# WIDTH = 700#amount of pixels
# HEIGHT = 700
# colors = {"white":(255,255,255), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
# clr = colors.get("white")

# #create a display
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("My First Game") # title of the window

# #images
# bg = pygame.image.load("PygameFile\images1\\bgSmaller.jpg")
# char = pygame.image.load("PygameFile\images1\PixelArtTutorial.png")
# char = pygame.transform.scale(char, (50,50))
# # screen.blit(bg, (0,0))
# # pygame.display.update()
# # pygame.time.delay(5000)

# #circle var
# cx = 350
# cy = 350
# rad = 25

# #square var
# hb = 50
# wb = 50
# xb = 325
# yb = 325
# square = pygame.Rect(xb,yb,wb,hb) #create the object to draw

# #char var
# charx = xb
# chary = yb

# #inscribed square
# ibox = rad*math.sqrt(2)
# xig = cx-(ibox/2)
# yig = cy-(ibox/2)
# insSquare=pygame.Rect(xig,yig,ibox,ibox)

# #bounce
# mountainSquare = pygame.Rect(250, 320, 180, 250)

# #Game Code
# speed = 2
# run = True
# background = colors.get("grey")

# def menu():
#     screen.fill(colors.get("white"))
#     menu = TITLE_FONT.render("Menu", 1, colors.get("black"))
#     xd = WIDTH//2 - (menu.get_width()//2)
#     screen.blit(menu, (xd, 50))\
    
#     inst_button = pygame.Rect(100, 200, 150, 50)
#     setting_button = pygame.Rect(300, HEIGHT//3, 115, 50)
#     game1_button=pygame.Rect(500,200,100,50)
#     game2_button=pygame.Rect(100,400,100,50)
#     sb_button=pygame.Rect(300,HEIGHT//2,150,50)
#     exit_button=pygame.Rect(500,HEIGHT//2,100,50)

    
#     pygame.draw.rect(screen, colors.get("red"), inst_button)
#     pygame.draw.rect(screen, colors.get("orange"), setting_button)
#     pygame.draw.rect(screen, colors.get("yellow"), game1_button)
#     pygame.draw.rect(screen, colors.get("green"), game2_button)
#     pygame.draw.rect(screen, colors.get("blue"), sb_button)
#     pygame.draw.rect(screen, colors.get("purple"), exit_button)

#     #render
#     text1 = MENU_FONT.render("Instructions", 1, colors.get("black"))
#     text2 = MENU_FONT.render("Settings", 1, colors.get("black"))
#     text3 = MENU_FONT.render("Game 1", 1, colors.get("black"))
#     text4= MENU_FONT.render("Game 2", 1, colors.get("black"))
#     text5 = MENU_FONT.render("Score Board", 1, colors.get("black"))
#     text6 = MENU_FONT.render("Exit", 1, colors.get("black"))
   
#     screen.blit(text1, (120, 410)) #
#     screen.blit(text2, (320, 410))
#     screen.blit(text3, (520, 410))
#     screen.blit(text4, (120, 610))
#     screen.blit(text5, (320, 610))
#     screen.blit(text6, (520, HEIGHT//2+ 10)) 
#     pygame.display.update()
    

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 print("you quit")
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mousePos = pygame.mouse.get_pos()
#                 mx = mousePos[0]
#                 my = mousePos[1]
#                 if inst_button.collidepoint(mx, my):
#                     instruction()
                





# def instruction():
#     #title font
#     screen.fill(colors.get("white"))
#     Title = TITLE_FONT.render("Instructions", 1, colors.get("black"))
#     xd = WIDTH//2 - (Title.get_width()//2)
#     screen.blit(Title, (xd, 50))\

#     #Instructions File
#     myFile = open("PygameFile\inst2.txt", "r")
#     content = myFile.readlines()

#     #print instructions
#     yi = 150
#     for line in content:
#         Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
#         screen.blit(Insctruc, (40, yi))
#         pygame.display.update()
#         pygame.time.delay(50)
#         yi += 40
    
#     #creating buttons
#     Button_1 = pygame.Rect(200, 400, 100, 50)
#     Button_2 = pygame.Rect(400, 400, 100, 50)
#     pygame.draw.rect(screen, colors.get("pink"), Button_1)
#     pygame.draw.rect(screen, colors.get("pink"), Button_2)

#     #render yes and no
#     text1 = MENU_FONT.render("Yes", 1, colors.get("black"))
#     text2 = MENU_FONT.render("No", 1, colors.get("black"))
#     screen.blit(text1, (225, 410))
#     screen.blit(text2, (425, 410))
#     pygame.display.update()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 print("you quit")
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mousePos = pygame.mouse.get_pos()
#                 mx = mousePos[0]
#                 my = mousePos[1]
#                 if Button_1.collidepoint(mx, my):
#                     return True
#                 if Button_2.collidepoint(mx, my):
#                     return False

# #functions
# menu()
# run = instruction()

# #main Game
# while run:
#     # screen.fill(background)
#     pygame.draw.rect(screen, colors.get("white"), mountainSquare)
#     screen.blit(bg, (0,0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             print("you quit")
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mousePos = pygame.mouse.get_pos()
#             # print(mousePos)
#     keys = pygame.key.get_pressed() #allow us to see what key was pressed

    

#     #square movement
#     if keys[pygame.K_d] and square.x < WIDTH-wb:
#         square.x += speed
#         charx += speed
#     if keys[pygame.K_a] and square.x > 0:
#         square.x -= speed
#         charx -= speed
#     if keys[pygame.K_s] and square.y < HEIGHT-hb:
#         square.y += speed
#         chary += speed
#     if keys[pygame.K_w] and square.y > 0:
#         square.y -= speed
#         chary -= speed

#     #circle and inscribed square movement
#     if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
#         cx += speed
#         insSquare.x += speed
#     if keys[pygame.K_LEFT] and cx > 0+rad:
#         cx -= speed
#         insSquare.x -= speed
#     if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
#         cy += speed
#         insSquare.y += speed
#     if keys[pygame.K_UP] and cy > 0+rad:
#         cy -= speed
#         insSquare.y -= speed
    
#     #circle square collide
#     if square.colliderect(insSquare): 
#         print("BOOM")
#         cx = random.randint(rad, WIDTH-rad)
#         cy = random.randint(rad, HEIGHT-rad)
#         rad += 5
#         ibox = rad*math.sqrt(2)
#         xig = cx-(ibox/2)
#         yig = cy-(ibox/2)
#         insSquare=pygame.Rect(xig,yig,ibox,ibox)
    
#     #mountain collide square
#     if square.colliderect(mountainSquare):
#         square.x = 10
#         square.y = 10
#         charx = 10
#         chary = 10
    
#     #mountain collide circle
#     if insSquare.colliderect(mountainSquare):
#         cx = rad + 10
#         cy = rad + 10
#         ibox = rad*math.sqrt(2)
#         xig = cx-(ibox/2)
#         yig = cy-(ibox/2)
#         insSquare=pygame.Rect(xig,yig,ibox,ibox)

#     #rect(surface, color, object)
#     pygame.draw.rect(screen, colors.get("blue"), square)
#     pygame.draw.rect(screen, colors.get("blue"), insSquare)
#     screen.blit(char, (charx, chary))

#     #circle(surface, color, center, radius)
#     pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
    
#     pygame.display.update()
#     pygame.time.delay(5)











#This was the good Code 


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



from cgitb import text
from locale import CHAR_MAX
from re import T
from tkinter import Menu
import pygame, os, time, random, math
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
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#circle var
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
run = True
background = colors.get("grey")

def menu():
    screen.fill(colors.get("white"))
    menu = TITLE_FONT.render("", 1, colors.get("black"))
    xd = WIDTH//2 - (menu.get_width()//2)
    screen.blit(menu, (xd, 50))\
    
    inst_button = pygame.Rect(100, HEIGHT//3, 150, 50)
    setting_button = pygame.Rect(300, HEIGHT//3, 115, 50)
    game1_button=pygame.Rect(500,HEIGHT//3,100,50)
    game2_button=pygame.Rect(100,HEIGHT//2,100,50)
    sb_button=pygame.Rect(300,HEIGHT//2,150,50)
    exit_button=pygame.Rect(500,HEIGHT//2,100,50)

    
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
                    instruction()
                # if setting_button.collidepoint(mx,my):

                



def instruction():
    #title font
    screen.fill(colors.get("white"))
    Title = TITLE_FONT.render("Instructions", 1, colors.get("black"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))\

    #Instructions File
    myFile = open("PygameFile\inst2.txt", "r")
    content = myFile.readlines()

    #print instructions
    yi = 150
    for line in content:
        Insctruc = MENU_FONT.render(line[0:-1], 1, colors.get('black'))
        screen.blit(Insctruc, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi += 40
    
    #creating buttons
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_1)
    pygame.draw.rect(screen, colors.get("pink"), Button_2)

    #render yes and no
    text1 = MENU_FONT.render("Yes", 1, colors.get("black"))
    text2 = MENU_FONT.render("No", 1, colors.get("black"))
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint(mx, my):
                    return True
                if Button_2.collidepoint(mx, my):
                    return False

#functions
menu()
run = instruction()

#main Game
while run:
    # screen.fill(background)
    pygame.draw.rect(screen, colors.get("white"), mountainSquare)
    screen.blit(bg, (0,0))
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
    
    #mountain collide square
    if square.colliderect(mountainSquare):
        square.x = 10
        square.y = 10
        charx = 10
        chary = 10
    
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
    screen.blit(char, (charx, chary))

    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, colors.get("red"), (cx, cy), rad)
    
    pygame.display.update()
    pygame.time.delay(5)








































