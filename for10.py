#Find the sum of all odd numbers from 1 to N.
n=int(input("Enter a number"))
sum=0
for x in range(1,n+1,2):
    sum=sum+x
print(sum)