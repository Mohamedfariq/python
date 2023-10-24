list1=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    x=input('Enter the element : ')
    list1.append(x)
x=int(input("Enter the element to find the index : "))
for i in range(len(list1)):
    if list1[i]==x:
        print("Index of",x,"is",i)
    
