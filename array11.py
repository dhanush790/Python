#Program to Remove Duplicate Elements from an Array
n=int(input("Enter a number"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a num")))
result=[]
for i in arr:
    if i not in result:
        result.append(i)
for i in result:
    print(i,end=" ")