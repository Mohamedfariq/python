n=int(input())
count=0
for i in range(n):
    count+=1
for i in range(n-(n-1),n+1,1):
    print(str(i)*count)
    count=count-1
