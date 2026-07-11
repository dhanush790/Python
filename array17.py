#Program to Count Even and Odd Elements in an Array
n=int(input("Enter a n:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a array:")))
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
        
print("Count of even",even)
print("count of odd",odd)