list1=[]
n=int(input("Number of elements : "))
for i in range(n):
    x=input("Element to be added: ")
    list1.append(x)
print(list1)
new_list=[]
i=0
while i<len(list1):
    y=list1[i].replace(",",".")
    new_list.append(y)
    i+=1
print(new_list)
print(max(new_list))
    

    
