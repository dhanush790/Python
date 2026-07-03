#Write a function to find the sum of digits of a number.
def sum(n):
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
    

num=int(input("Enter a num"))
print(sum(num))
  