#Cassie Rosa
#Program about using files, datetime
# 'r'  read
#'a' append
#'w' write
#open a file and make sure to close 
#datetime

from datetime import datetime
import random
import os, datetime

os.system('cls')

date=datetime.datetime.now() #this is how to show the current date in the terminal 
print(date)
print(date.strftime("%m / %d / %y"))

name="Cass"
sce=200

#create a line of string put into file 
scrline=name+"\t"+str(sce)+"\t " +date.strftime("%m / %d / %y")+ "\n " #this creates and enter space in file 
print(scrline)

#create a file
myFile=open("scre.txt", 'w')
myFile.write(scrline)
myFile.close()
#Create a new line 
name="peter"
sce=132
scrline=name+"\t"+str(sce)+"\t " +date.strftime("%m / %d / %y")+ "\t "
#this append file ---add lines to file 
myFile=open("scre.txt", 'a')
myFile.write(scrline)
myFile.close()

#read file 
myFile=open("scre.txt", 'r')
stuff=myFile.readlines()
myFile.close()

for line in stuff:
    print(line)