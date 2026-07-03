#Write a function to check whether a number is a Perfect number.
def perfect(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total=total+i
    if total==n:
        return "Perfect"
    else:
        return "Not"
num=int(input("Enter a num"))
print(perfect(num))
        