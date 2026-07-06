#Write a Function to Print All Perfect Numbers Between 1 and N
def perfect(n):
    for num in range(1,n+1):
        total=0
        for i in range(1,num):
            if num%i==0:
                total+=i
        if total==num:
            print(num)
n=int(input("Enter a number"))
perfect(n)