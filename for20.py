#Generate the Fibonacci series up to N terms.
num=int(input("Enter a number"))
a=0
b=1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c