#Cassie Rosa
#learning basic pygame functions 

import pygame, os, time
pygame.init()
os.system('cls')

WIDTH= 700 #amount of pixals
HEIGHT= 700
#red green blue



Color ={"white":(255,255,255),"peach":(255,102,102),"dreamsical":(255,178,102),"banana":(255,255,102),}
clr=color.get("white") 
#this is like a color dictionary 



#create a display screen
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #dont forget double paranth- input one value like cordinate
pygame.display.set_caption("My first game") #title/caption of window 
pygame.time.delay(3000) #this is 3 seconds

blueClr= (0,0,255) #this just add color 
redClr=(255,0,0)
purpClr= (200,10,200)
screen.fill(blueClr) # this will add the color to the screen but must update 
pygame.display.update() # this will update  must do after every change 
pygame.time.delay(3000)

#to create a square 
hb=50
wb=50
xb=100
yb=300
square=(xb,yb,wb,hb)




run=True
while run:
    screen.fill(redClr)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT: #make it so that you can quit photo using the X in top right corner 
            print("you quit")
    #rect (surface, color, object)        
    pygame.draw.rect(screen,blueClr,square)#add square to screen- must be in right order *like stacking order  
    #circle (surface, color,center, radius)
    pygame.draw.circle(screen,purpClr, (350,350), 25)
    pygame.display.update() #if dont break/quit will continue forever






