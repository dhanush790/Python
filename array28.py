#Write a program to find the leader elements in an array.
n=int(input("Enter a num: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr: ")))
for i in range(n):
    leader=True
    for j in range(i+1,n):
        if arr[i]<=arr[j]:
            leader=False
            break
if leader:
    print(arr[i],end=" ")