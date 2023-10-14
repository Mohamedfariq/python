s=input('Enter a string : ')
list1=[]
sum=0
for i in s:
    x=list1.append(i)
for i in list1:
    if i>="A" and i<="Z":
        sum=sum+ord(i)
print(sum)
    
