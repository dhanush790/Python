#Check whether a number is an Armstrong number.
num=int(input("Enter a number"))
temp=num
sum=0
while temp>0:
    digit=num%10
    sum=sum+digit**3
    temp=temp//10
if temp==sum:
    print("Amstrong")
else:
    print("Not")