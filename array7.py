#Write a program to reverse an array.
n=int(input("Enter a number"))
arr=[]
for i in range(n):
    arr.append(int(input('Enter a num')))
print("Reversed array")
for i in range(n-1,-1,-1):
    print(arr[i],end=" ")