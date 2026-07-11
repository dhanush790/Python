#Program to Copy One Array into Another
n=int(input("Enter a n:"))
arr1=[]
for i in range(n):
    arr1.append(int(input("Enter arr1:")))
arr2=[]
for i in arr1:
    arr2.append(i)
print("Original array")
for i in arr1:
    print(i,end=" ")
print("\nCopied array")
for i in arr2:
    print(i,end=" ")