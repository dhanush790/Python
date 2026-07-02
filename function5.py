#Write a function to check whether a number is prime.
def prime(n):
    if n<=1:
        return "Not prime"
    for i in range(2,n):
        if n%i==0:
            return "not prime"
    return "prime"
n = int(input("Enter a number: "))
print(prime(n))
        