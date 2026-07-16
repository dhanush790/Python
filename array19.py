#Program to Find the Missing Number in an Array
n=int(input("Enter a num"))
arr=[]
print("Enter",n-1,"elements")
for i in range(n-1):
    arr.append(int(input()))
total=n*(n+1)//2
sum=0
for i in arr:
    sum+=i
missing=total-sum
print("Missing Number= ",missing)