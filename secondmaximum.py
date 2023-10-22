list1=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    x=input('Enter the element : ')
    list1.append(x)
maximum=list1[0]
secondmax=list1[1]
for i in list1:
    if i>maximum:
        secondmax=maximum
        maximum=i
    elif i>secondmax and i!=maximum:
        secondmax=i      
print(secondmax)
    
    
