#Write a function to find the GCD of two numbers.
def gcd(num1,num2):
    gcd=1
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            gcd=i
    return gcd
num1=int(input("Enter a num1"))
num2=int(input("Enter a num2"))
print(gcd(num1,num2))