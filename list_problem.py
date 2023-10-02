list1=[]
n=int(input("Enter the value : "))
for i in range(n,(n*n)+1):
    list1.append(i)
print(list1)
odd_list=[]
even_list=[]
for i in list1:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Odd list = ",odd_list)
print("Even list = ",even_list)

print(odd_list[0:n])
print(even_list[0:n])
    
