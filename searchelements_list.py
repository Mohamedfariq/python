list1=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    x=input("Enter the element : ")
    list1.append(x)
p=input("Enter the prefix : ")
for i in range(len(list1)):
    if(list1[i].startswith(p)):
        print(list1[i])
        break
