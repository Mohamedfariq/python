def prime(n,k):
    
    for i in range(2,k):
        
        if (k%i)==0:
            break
    else:
        l.append(k)
        
    if len(l)==n:
        return l
    
    else:
        return prime(n,k+1)
        
l=[]
k=2

n=int(input("Enter the number of prime numbers to be printed: "))

print(prime(n,k))
    
    






