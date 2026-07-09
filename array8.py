#Write a program to sort an array in ascending order.
n=int(input("Enter a num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a num")))
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(n):
    print(arr[i],end=" ") 