#Cassie Rosa
# How To calculate a persons BMI

import os 
os .system('cls')

weight= int(input("your weight in pounds: ")) #how perons puts their wight in the terminal 
multiply= weight * 703
height= int(input("your height in inches: ")) # how person puts their height in terminal 
multiply1= height * height 
divide= multiply / multiply1
print (divide) #the BMI in terminal  --- divide is your BMI result 

if (divide < 18.5): # this will check if you number 
    print ("your underwight")

if (divide > 25 ):
    print ("your overweight")

if (divide >= 18.6 and divide <= 24.9):#how do you do inbetween like healthy 18
    print ("your healthy")

if (divide < 18.5 or divide > 25):
    print ("your unhealthy")