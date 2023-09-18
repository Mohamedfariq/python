n = int(input("Enter the number of fibonacci series : "))

a=0
b=1

if n==1:
    print(a)
else:
    print(a)
    print(b)

for i in range(2,n):
    x=a+b
    print(x)
    a,b=b,x
