#Cassie Rosa
# integer and float work
#how to find odd or even
#how to find a mulitple of integer
#how to find last digit

#Write a code that find if the number input by the user is even or odd is the number is multiple of 3 or 5

import os 
os .system('cls')

num=int(input("any integer")) #can imput in terminal any integer (whole number)

if num % 2 ==0: #this checks if even 
    print("Integer is even")
else: print("Integer is odd")

if num % 3 == 0: #this checks if multiple of 3 becasue there would be no remainder
    print("this integer is a multiple of 3")

if num % 5 ==0: #this checks if mulitple of 5 becasue there no remainder
    print ("this integer is multiple of 5")

if num % 3 == 0 and num % 5 ==0: #this checks if integer is both miltiple 5 and 3 (15)
    print("this integer is a multiple of both")

print(num%10) #this finds last digit of a number 
print(num%100)

