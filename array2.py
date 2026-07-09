#Write a program to find the average of array elements.
n=int(input("Enter a num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a element")))
total=0
for i in arr:
    total+=i
avg=total/n
print("Average:",avg) 