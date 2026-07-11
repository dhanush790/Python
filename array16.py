#Program to Find the Maximum and Minimum Elements in an Array
n=int(input("Enter a n:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr:")))
maximum=arr[0]
minimum=arr[0]
for i in arr:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print("Maximum",maximum)
print("Minimum",minimum)
    
