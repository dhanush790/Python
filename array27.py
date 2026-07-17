#Write a program to merge two sorted arrays into a single sorted array.
n1=int(input("Enter a num: "))
arr1=[]
for i in range(n1):
    arr1.append(int(input("Enter a arr1: ")))
n2=int(input("Enter a num: "))
arr2=[]
for i in range(n2):
    arr2.append(int(input("Enter a arr2: ")))
arr3=arr1+arr2
n=n1+n2
for i in range(n):
    for j in range(i+1,n):
        if arr3[i]>arr3[j]:
            temp=arr3[i]
            arr3[i]=arr3[j]
            arr3[j]=temp
for i in arr3:
    print(i,end=" ")
