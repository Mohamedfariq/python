def binarysearch(l,key):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            print("Element found")
            break
        else:
            if l[mid]<key:
                low=mid
            elif l[mid]>key:
                high=mid
    else:
        print("Element not found")
            
    return " "
l=[]
n=int(input("Enter the number of elements :"))
for i in range(n):
    x=int(input("Enter an element to be added :"))
    l.append(x)
l=sorted(l)
key=int(input("Enter an element to be searched :"))
print(binarysearch(l,key)) 

