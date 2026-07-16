#Write a program to move all zeros to the end of an array.
n=int(input("Enter a num: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr: ")))
result=[]
for i in arr:
    if i!=0:
            result.append(i)
while len(result)<n:
    result.append(0)
print("New array")
for i in result:
    print(i,end=" ")