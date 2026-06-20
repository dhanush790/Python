#Find the sum of all even numbers from 1 to N.
n=int(input("Enter a number"))
sum=0
for x in range(2,n+1,2):
    sum=sum+x
print(sum)