#Write a program to find the smallest element in an array.
n=int(input("Enter an num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a element")))
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print("smallest:",smallest)