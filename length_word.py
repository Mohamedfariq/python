list1=[]
n=int(input("Number of elements : "))
for i in range(n):
    x=str(input("Element to be added: "))
    list1.append(x)
print(list1)
i=0
while i<len(list1):
    print(len(list1[i]),end=',')
    i+=1
    
    
