numbers=[]
n=int(input("Enter the number of values : "))
for i in range(n):
    a=int(input("\n Enter the value : "))
    numbers.append(a)
    
print("\n Values = ",numbers)

x=max(numbers)
try:
    numbers.pop(x)
except IndexError:
    print()
y=max(numbers)
print("\n",y)

