# #Cassie Rosa 
# #using video to code moving images 
# #using pre-made code from the video 

import pygame
pygame.init()

win = pygame.display.set_mode((480,480))
pygame.display.set_caption("First Game")

#this imports the images and creates list to more easily get the image you want 
walkRight = [pygame.image.load('PygameFile\Moving IMages\R1.png'), pygame.image.load('PygameFile\Moving IMages\R2.png'), pygame.image.load('PygameFile\Moving IMages\R3.png'), pygame.image.load('PygameFile\Moving IMages\R4.png'), pygame.image.load('PygameFile\Moving IMages\R5.png'), pygame.image.load('PygameFile\Moving IMages\R6.png'), pygame.image.load('PygameFile\Moving IMages\R7.png'), pygame.image.load('PygameFile\Moving IMages\R8.png'), pygame.image.load('PygameFile\Moving IMages\R9.png')]
walkLeft = [pygame.image.load('PygameFile\Moving IMages\L1.png'), pygame.image.load('PygameFile\Moving IMages\L2.png'), pygame.image.load('PygameFile\Moving IMages\L3.png'), pygame.image.load('PygameFile\Moving IMages\L4.png'), pygame.image.load('PygameFile\Moving IMages\L5.png'), pygame.image.load('PygameFile\Moving IMages\L6.png'), pygame.image.load('PygameFile\Moving IMages\L7.png'), pygame.image.load('PygameFile\Moving IMages\L8.png'), pygame.image.load('PygameFile\Moving IMages\L9.png')]
bg = pygame.image.load('PygameFile\Moving IMages\\bg.jpg')
char = pygame.image.load('PygameFile\Moving IMages\standing.png') 

clock=pygame.time.Clock() #this helps frame rate 

x = 50
y = 400
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  # This will draw our background image at 0
    if walkCount +1>=27:
        walkCount=0
    if left :
        win.blit(walkLeft[walkCount//3],(x,y))
        walkCount +=1
    elif right:
        win.blit(walkRight[walkCount//3],(x,y))
        walkCount +=1
    else:
        win.blit(char,(x,y))
    

    pygame.display.update() 
    


run = True

while run:
    clock.tick(27) # this will do frames per second 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: # If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False 
            left = False 
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() #must end with the def (not sure why)
    
    
pygame.quit()













































































# import pygame
# pygame.init()

# win = pygame.display.set_mode((500,500))
# pygame.display.set_caption("First Game")

# walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
# walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
# bg = pygame.image.load('bg.jpg')
# char = pygame.image.load('standing.png')

# x = 50
# y = 425
# width = 40
# height = 60
# vel = 5

# isJump = False
# jumpCount = 10

# left = False
# right = False
# walkCount = 0


# def redrawGameWindow():
#     global walkCount
#     win.blit(bg, (0,0))  # This will draw our background image at (0,0)
#     pygame.display.update() 
    

# #main game loop
# run = True
# while run:
#     pygame.time.delay(50)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     keys = pygame.key.get_pressed()
    
#     if keys[pygame.K_LEFT] and x > vel: 
#         x -= vel

#     if keys[pygame.K_RIGHT] and x < 500 - vel - width:  
#         x += vel
        

 

#     if not(isJump): 
#         if keys[pygame.K_SPACE]:
#             isJump=True
#     else:
#         if jumpCount >= -10:
#             neg=1
#             if jumpCount <0:
#                 neg=-1
#             y -= (jumpCount **2) * 0.5 *neg
#             jumpCount -= 1
#         else: 
#             jumpCount = 10
#             isJump = False


# #missing bottum peice 
#     win.fill((0,0,0))
#     pygame.draw.rect
    
    
# pygame.quit()