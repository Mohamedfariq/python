a=input("Enter your birth date in DD/MM/YYYY format :")
b=input("Enter today's date in DD/MM/YYYY format :")
x=a.split("/")
y=b.split("/")

def age(a,b,x,y):
    
    z=int(y[2])-int(x[2])
    b=int(y[2])-int(x[2])-1
    
    if (int(y[0])==int(x[0]) and int(y[1])==int(x[1])):
        return "Age :",z

    if (int(y[1])>int(x[1]) and int(y[0])>=int(x[0])) :
        return "Age :",z
    
    else:
        return "Age :",b
    
print(age(a,b,x,y))
