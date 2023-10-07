base=int(input("Enter the base : "))
exp=int(input("Enter the exponent : "))
result=1
for i in range(exp):
    result=result*base
print("The value of",base,"^",exp,"is",result)
