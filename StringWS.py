#Cassie Rosa
#String Worksheet in groups using string arrays,  
#Exercise 1A: Create a string made of the first, middle and last character james---jms

import os 
os .system('cls')

message= "James"

print (message[0],end="") #gives me the J 

wordlength= len(message)  
middle = int(wordlength/2) #how to print middle character in message  (m)
#print(middle)
print (message[middle], end="")

#print (wordlength)
print (message[wordlength-1]) #this will give the s 


#Exercise 1B: Create a string made of the middle three characters-- JhonDipPeta ->dip 

message2= "JhonDipPeta"


wordlength2= len(message2)  
middle2 = int(wordlength2/2) #how to print middle character in message  (D)
print (message2[middle2 -1], end="")
print (message2[middle2], end="")
print (message2[middle2+1], )


#Part 2 Exersise 1B: JaSonAy ->Son

message3= "JaSonAy"
#print (message3[2],end="")
#print (message3[middle3 -1], end="")
wordlength3= len(message3)  
middle3 = int(wordlength3/2) #how to print middle character in message  (D)
print (message3[middle3 -1], end="")
print (message3[middle3], end="")
print (message3[middle3 +1], )
#print (message3[4],)


#Exercise 2: Append new string in the middle of a given string

string1= "ault"
string2="kelly"

wordlength4= len(string1)
middle4= int(wordlength4/2)
print(string1[0:middle]+string2 +string1[middle:]) #splits ault by using letters 0 to middle

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string

string3= "American"
string4= "Japan"

print (string3[0],end="") #first letter (A)
print (string4[0],end="") #first letter (J)
wordlength5= len(string3)
wordlength6=len(string4)
middle5= int(wordlength5/2)
middle6=int(wordlength6/2)
print (string3[middle5 -1],end="")
#print (string3[middle],end="") 
#print (string4[middle],end="") #middle of japan (p)
print (string4[middle6:])

#Exercise 4: Arrange string characters such that lowercase letters should come first --> PyNaTive to yaivePNT

string5="PyNaTive"

print (string5[1],end="")

wordlength7= len(string5)  
middle7 = int(wordlength7/2) 
print (string5[middle7 -1], end="")
print (string5[middle7 +1 :], end="")

print (string5[0],end="")
print (string5[2],end="")
print (string5[middle7], end="")









