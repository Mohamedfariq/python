n=int(input()) #Number of inputs
from math import *
for i in range(n):
    
    t=input() #Getting quadratic equation as input from user
    
    x=t.split("x^2") # To get the value of a (coefficient of x^2)
    
    s=""
    for i in x[1:]:
        s+=i
    y=s.split("x") # To get the value of b (coefficient of x)
    
    s1=""
    for j in y[1:]:
        s1+=j
    z=s1.split("=") # To get the value of c
    
    #value of a
    if x[0]=='':
        a=1
    else:
        a=int(x[0])
        
    #value of b    
    if y[0]=='':
        b=1
    else:
        b=int(y[0])
        
    #value of c    
    c=int(z[0])

    #To get the the first root
    quad1= sqrt((b*b) - (4*a*c)) -(b)
    quad2=2*a

    #To get the second root
    quad3= -(sqrt((b*b) - (4*a*c))) -(b)
    quad4=2*a

    #print the roots
    print(int(quad3/quad4),int(qua




