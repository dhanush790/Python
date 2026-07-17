#Write a program to find the majority element in an array.
n=int(input("Enter a num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a arr: ")))
found=False
for i in range(n):
    count=0
    for j in range(n):
        if arr[i]==arr[j]:
            count+=1
    if count > n // 2:
        print("Majority Element:", arr[i])
        found = True
        break

if found == False:
    print("No Majority Element")