#Print the First N Multiples of a Given Number
num=int(input("Enter a number"))
n=int(input("Enter multiples"))
for i in range(1,n+1):
    print(num*i)