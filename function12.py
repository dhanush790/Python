#Write a function to check whether a number is an Armstrong number.
def amstrong(n):
    temp=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**3
        n//10
        if temp==sum:
            return "Amstrong"
        else:
            return "Not"

num=int(input("Enter a number"))

print(amstrong(num))

    