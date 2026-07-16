#Write a program to rotate an array to the right by K positions.
n=int(input("Enter a num: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr: ")))
K=int(input("Enetr a K"))
for i in range(K):
    temp=arr[n-1]
    for j in range(n-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=temp
print("Right rotation")
for i in arr:
    print(i,end=" ")
    