list1=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    x=input('Enter the element : ')
    list1.append(x)
minimum=list1[0]
secondmin=list1[1]
for i in list1[1:]:
    if i<minimum:
        secondmin=minimum
        minimum=i
    elif i<secondmin:
        secondmin=i      
print(secondmin)
    
    
