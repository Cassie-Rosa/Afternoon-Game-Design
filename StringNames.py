
#Cassie Rosa
#String Practice and different methods

import os 
os.system('cls')


message= "i am tired" #string array of characters 
#       0 1 2 3 4 5 6 7 8 ... arrays begin at zero

print (message)
print (message[5])


wordlength= len(message)
print (wordlength)
print (message[wordlength-1]) #finds the last letter in message--(string) no matter word and length 

if message.isdigit(): #when using methods add dot at the end ----string site 
    sum = message + 3  #if message true
    print (sum)

else:                   #if statement false
    print(message + "so i nap") #concantination

print(message.upper())

if message.isupper():
    print(message)
else:
    message=message.upper()
    print (message)

middle = int(wordlength/2) #how to print middle character in message 
print(middle)
print (message(middle))

print(message[0:7]) #how to print charecters between 0-7 

