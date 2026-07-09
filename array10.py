#Program to Count the Occurrence of an Element in an Array
n=int(input("Enter a num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a number")))
count=int(input("Enter a number to count"))
c=0
for i in arr:
    if i==count:
        c+=1
print("Count:",c)