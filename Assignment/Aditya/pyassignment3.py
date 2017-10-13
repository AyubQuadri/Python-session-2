# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 08:18:32 2017

@author: aditya
"""
#1.Single conditional statements
a=12
if (a<5):
    print ("a is less than 5")
elif(a==5):
    print ("a is equal to 5")
else:
    print ("a is greater than 5")
    
name='Alice'
age=12
if(name=='Alice' and age<=12):
    print ("Hi Alice")
else:
    print ("You r not Alice kiddo")
    
#multiple conditional statements
print("Enter username:")
username=input()
print("Enter password:")
password=input()

if(username=='Alice'):
    if(password=='12345'):
        print("Welcome Alice!")
elif(username=='spyder'):
    if(password=='a123'):
        print("welcome spyder!")
else:
    print("invalid username or password") 

#2.For loop program

for i in range(1,10):
    print(i)
    
#while loop program
count=1
while(count<10):
    print ("The count is:", count)
    count+=1
print ("Bye")    

#3.Program for break,continue,pass
number = 0
for number in range(10):
   number = number + 1
   if number == 5:
      break    
   print('Number is ', number)
print('Out of loop')


number = 0
for number in range(10):
   number = number + 1
   if number == 5:
       continue
   print('Number is ',number)
print('Out of loop')


number = 0
for number in range(10):
   number = number + 1
   if number == 5:
      pass
   print('Number is ' + str(number))
print('Out of loop')
























