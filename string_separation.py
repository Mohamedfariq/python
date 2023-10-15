string="( () ((()()())) (()) ()"
x=string.split()
print(x)
i=0
while i<len(x):
    if len(x[i])%2!=0:
        try:
            print(x[i]+x[i+1],end=' ')
        except IndexError:
            print()
    if len(x[i])%2==0:
        try:
            print(x[i],end=' ')
        except IndexError:
            print()
    i=i+1
