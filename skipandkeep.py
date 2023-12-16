n,k=input().split()#n- length of array, k- skip and keep value
x=input().split()
l=[]
a=0
b=int(k)
for i in range(int(n)):
    m=x[a:b]
    if m==[]:
        break
    else:
        l.append(m)
        a=a+(2*int(k))
        b=b+(2*int(k))
for i in l:
    for j in range(len(i)):
        print(i[j],end=' ')
