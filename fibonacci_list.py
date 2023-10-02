n=int(input("Enter the value : "))
fib=[0,1]
for i in range(len(fib),n):
    fib.append(fib[-1]+fib[-2])
print(fib)
