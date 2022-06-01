#Cassie Rosa
# How To calculate a persons BMI

import os 
os .system('cls')

weight= int(input("your weight in pounds: ")) #how perons puts their wight in the terminal 
multiply= weight * 703
height= int(input("your height in inches: ")) # how person puts their height in terminal 
multiply1= height * height 
divide= multiply / multiply1
print (divide) #how the BMI in terminal 

if (divide < 18.5):
        print ("your underwight")

if (divide > 25):
    print ("your overweight")


