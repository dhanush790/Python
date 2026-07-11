#Program to Merge Two Arrays
n1=int(input("Enter a n1"))
arr1=[]
for i in range(n1):
    arr1.append(int(input("Enter a num")))
n2=int(input("Enter a n2"))
arr2=[]
for i in range(n2):
    arr2.append(int(input("Enter a num")))
arr3=arr1+arr2
for i in arr3:
    print(i,end=" ")