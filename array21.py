#Program to Find the Frequency of Each Element in an Array
n=int(input("Enter a num: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr: ")))
visited=[]
for i in arr:
    if i not in visited:
        print(i ,"=", arr.count(i))
        visited.append(i)