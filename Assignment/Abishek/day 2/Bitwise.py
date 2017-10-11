# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 23:30:37 2017

@author: abishekcm
"""

print('Enter the value a')
a= input()
a=int(a)
print('Enter the value b')
b= input()
b=int(b)
c= a & b 
print ('The & operation of a and b is:',c)
d=a | b
print ('The | operation of a and b is:',d)
e= a^b
print('The ^ operation of a and b is:',e)
f= a<<1
print('The value is',f)
g= a>>1
print('The value is:',g)
