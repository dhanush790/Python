#Write a program to find the second largest element in an array.
n=int(input("Enetr a num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter a num")))
second_largest=arr[0]
largest=arr[0]
for i in arr:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i
print("Second largest:",second_largest)