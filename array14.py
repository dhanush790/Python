#Program to Insert an Element at a Given Position in an Array
n=int(input("Enter a n:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr:")))
element=int(input("Enter a element"))
position=int(input("Enter a position"))

arr.insert(position-1,element)
print("New array")
for i in arr:
    print(i,end=" ")