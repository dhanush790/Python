#Program to Find the Common Elements in Two Arrays
n1=int(input("Enter a n1"))
arr1=[]
for i in range(n1): 
    arr1.append(int(input("Enter arr1:")))
n2=int(input("Enter arr2"))
arr2=[]
for i in range(n2):
    arr2.append(int(input("Enter arr2")))
print("Common Elements")
for i in arr1:
    if i in arr2:
        print(i,end=" ")