#Program to Delete an Element from an Array
n=int(input("Enter a n:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr:")))
element=int(input("Enter a element"))
if element in arr:
    arr.remove(element)
print("New array")
for i in arr:
    print(i,end=" ")