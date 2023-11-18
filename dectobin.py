l=[]
n=int(input("Enter the decimal number :"))
a=n
for i in range(n):
    y=n//2
    x=n%2
    n=y
    l=l+[x]
    if n==0:
        break
print("Binary value of",a)
for i in l[::-1]:
    print(i,end=' ')
