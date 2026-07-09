#Write a program to find the sum of all elements in an array. 
n=int(input("Enter a num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element")))
total=0
for i in arr:
    total+=i
print("Sum:",total)