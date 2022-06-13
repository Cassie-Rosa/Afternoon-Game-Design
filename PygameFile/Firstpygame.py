#Cassie Rosa
#learning basic pygame functions 

import pygame, os, time, math
pygame.init()
os.system('cls')
import random

WIDTH= 700 #amount of pixals
HEIGHT= 700
#red green blue



Color ={"white":(255,255,255),"peach":(255,102,102),"dreamsical":(255,178,102),"banana":(255,255,102),}
clr=Color.get("peach") 
#this is like a color dictionary 

backgrnd=clr

#create a display screen
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #dont forget double paranth- input one value like cordinate
pygame.display.set_caption("My first game") #title/caption of window 
#pygame.time.delay(3000) #this is 3 seconds

blueClr= (0,0,255) #this just add color 
redClr=(255,0,0)
purpClr= (200,10,200)
# screen.fill(blueClr) # this will add the color to the screen but must update 
# pygame.display.update() # this will update  must do after every change 
# pygame.time.delay(3000)

#to create a square 
hb=50
wb=50
xb=100
yb=300
cx=350
cy=350
rad=25
#must define square as rectangle 
square= pygame.Rect(xb,yb,wb,hb)

#Describes square 
ibox=rad*math.sqrt(2)
xig=cx-(ibox/2)
yig=cy-(ibox/2)
insSquare=pygame.Rect(xig, yig,ibox,ibox)

# 

#declare a variable for moving 
speed = 2

run=True
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT: #make it so that you can quit photo using the X in top right corner 
            print("you quit")
            run=False
    # This is how you move a shape using AWSD and <>^down
    key=pygame.key.get_pressed() #this provides a list of all keys 
    if key[pygame.K_a] and square.x > speed:
        square.x -= speed
    if key[pygame.K_d] and square.x < WIDTH-(wb+speed):
        square.x += speed
    if key[pygame.K_s] and square.y < HEIGHT-(hb+speed):
        square.y += speed
    if key[pygame.K_w] and square.y > speed:
        square.y -= speed

    if key[pygame.K_LEFT] and cx > (speed +rad):
        cx -= speed
        insSquare.x +=speed 
    if key[pygame.K_RIGHT] and cx < WIDTH-(rad+speed):
        cx += speed
        insSquare.x +=speed
    if key[pygame.K_DOWN] and cy < HEIGHT-(rad+speed):
        cy += speed
        insSquare.y +=speed
    if key[pygame.K_UP] and cy > (speed +rad):
        cy-= speed
        insSquare.y +=speed

    # if square.collidepoint((cx,cy)):
    if square.colliderect(insSquare):
        print("boom")
        cx=random.randint(rad,WIDTH-rad) 
        cy=random.randint(rad, HEIGHT-rad)
        rad += 5
        ibox=rad*math.sqrt(2)
        xig=cx-(ibox/2)
        yig=cy-(ibox/2)
        insSquare=pygame.rect(xig, yig,ibox,ibox)   

    #rect (surface, color, object)        
    pygame.draw.rect(screen,blueClr,square)#add square to screen- must be in right order *like stacking order  
    #circle (surface, color,center, radius)
    pygame.draw.circle(screen,purpClr, (cx,cy), rad) # instead of cordinate use a variable 
    pygame.draw.rect(screen,backgrnd ,insSquare)
    pygame.display.update() #if dont break/quit will continue forever








