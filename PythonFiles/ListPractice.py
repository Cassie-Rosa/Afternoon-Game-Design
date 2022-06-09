#Cassie Rosa
#Learn list, list func and meth, add elements, delete
#for loops
#random class

import os 
import random
os .system('cls')

#a list is an array is indexed, is changeable, is sizable 
#name and use []
mylist=[1,2,3,4,5]
#       0 1 2 3
#         -3 -2 -1  
print(mylist)
print(mylist[1]) #will print elem in posistion 1
print(mylist[1:3]) #will print elem 1, 2
print(mylist[-1]) #will print last elem
print(mylist[-3 :-1 ]) #will print 3-5 ***cant do -1:-3 becasue is going right to left not left to right

myfruits=["apple", "bananas", "kiwi", "papaya", "pear"] 
print(myfruits[:3]) #wil print the first 3 words 

lengthlist=len(myfruits) #number of elements is always one less than your last index
# print(lengthlist)
# print(myfruits[lengthlist-1])
# print (myfruits[0])
# print (myfruits[1])
# print (myfruits[2])

#for loops repeats specific number of times 
for elem in myfruits: #control the loop -- elem is a local var
    print(elem)
for elem in range (lengthlist-3): #if do just length will do whole list
    print(elem,end=" = ") #prints list equal ---- 0= apple 
    print(myfruits[elem])

# Add Elements 

if "apple" in myfruits:
    print("yes apple is in my list")

myfruits.append("pinapple") #how to add something to list --- append only adds elements to end of list 
print(myfruits[0:]) #this part print the normal list but the code above is what changed it

myfruits.insert(0,"orange")# insert --- puts element where you want it to go 
print (myfruits[0:])

mylist.extend(myfruits) #this will add  to lists together so my list + myfruits
print (mylist)

mylist.append(myfruits) #append will ad list insde of a list 
print(mylist)
print (mylist[5]) #will show just one side of list 
print(mylist[5][1]) #will show specific part on the one side of list 

myfruits[1]="hi" #this will replace the banana with hi 
print(myfruits)

#Random - random class use to get a random value
for i in range (10): #this is a loop to repeat an action 10 times 
    element=random.choice(myfruits) #this will choose a random fruit 
    print(element)