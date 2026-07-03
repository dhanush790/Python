#Write a function to check whether a number is a palindrome.
def palindrome(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    
    if temp==rev:
        print("palindrome") 
    else:
        print("not")
num=int(input("Enter a num"))
palindrome(num)
        