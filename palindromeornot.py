n=int(input("Enter a number : "))
rev=0
temp=n
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if rev==temp:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")

