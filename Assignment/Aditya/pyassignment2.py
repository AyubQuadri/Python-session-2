#1.Write a program to demonstrate logical 'AND','OR' operator 
a= True
b= False

c= a and b
print (c)
c= a and a 
print(c)

c= a or b
print(c)
c= b or b
print (c)

#Bitwise '&', '|' operators
c=2&3
print(c)
t=5|4
print(t)

#2.Write a code to take input from user and perform following tasks
print('enter a value')
a = input()
a=int(a)
print('enter b value')
b = input()
b=int(b)
#performing arithmetic operations
c = a+b
print(c)
c = a-b
print(c)
c=a*b
print(c)
c=a/b
print(c)
c=a%b
print(c)
c=a**b
print(c)
#Bitwise operations
c= a & b
print(c)
c=a|b
print(c)
c=a^b
print(c)
c=a<<b
print(c)
C=a>>b
print(c)
#Relational operations
5==5#true
5!=5#false
8>2#true
2<8#true
8>=2#true
7<=7#true
#logical operations
a= True
b= False

c= a and b
print (c)
c= a and a 
print(c)

c= a or b
print(c)
c= b or b
print (c)
#Assignment operations
a=2
print(a)
c+=2
print(c)
c-=2
print(c)
c*=2
print(c)

#3.Program to understand bitwise shift operation
print('enter any value')
a=input()
a=int(a)
print('enter another value')
b=input()
b=int(b)
c=a<<b
print(c)
c=a>>b
print(c)

#4.Multiply elements using bitwise shift operations .
a=5
c=a<<1
print(c*2)
print(c/2)
