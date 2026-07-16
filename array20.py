#Program to Find Unique Elements in an Array
n=int(input("Enter a num: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr:")))
for i in arr:
    if arr.count(i)==1:
        print(i)