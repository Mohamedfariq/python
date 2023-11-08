str1=sorted(input().lower())
list1=[chr(i) for i in range(97,123)]
count=0
for i in str1:
    if i==' ':
        count+=1
for i in range(count):   
    str1.remove(' ')
if str1==list1:
    print("It is a pangram")
else:
    print("It is not a pangram")
