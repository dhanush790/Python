#Write a program to find the pair of elements whose sum is equal to a given value.
n=int(input("Enter a num: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr: ")))
target_sum=int(input("Enter a target: "))
found=False
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target_sum:
            print(arr[i],arr[j])
            found=True
if found==False:
    print("No pair")
    
            
    
    