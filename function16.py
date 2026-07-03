#Function to Check Whether a Number is a Strong Number
def strong(n):
    temp=n
    total=0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        total=total+fact
        n=n//10
    if total==temp:
        return "Strong"
    else:
        return "Not"
num=int(input("Enter a num"))
print(strong(num))
        