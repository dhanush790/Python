n=int(input("Enter an num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a element")))
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("Largest:",largest)