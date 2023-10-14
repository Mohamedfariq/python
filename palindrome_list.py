def palindrome(string):
    list1=list(string)
    list2=[]
    i=1
    while i<=len(list1):
        list2.append(list1[-i])
        i=i+1
    if (list1==list2):
        print("palindrome")
    else:
        print("Not a palindrome")

    

