#Write a program to move all negative numbers to the beginning of an array.
n=int(input("Enter a num: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr: ")))
result=[]
for i in arr:
    if i<0:
        result.append(i)
for i in arr:
    if i>0:
        result.append(i )
print("New array")
for i in result:
    print(i,end=" ")
        