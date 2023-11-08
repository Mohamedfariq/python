list1=[chr(i) for i in range(97,123)]
str1 = list(input("Enter a string :").lower())
count=0
for i in str1 :
    if i not in str1:
        count +=1
        break 
if count==0:
    print("It is a panagram")
else:
    print("It is not a panagram")
