#Write a program to search for an element in an array.
n=int(input("Enter a num"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter element: ")))

key = int(input("Enter the element to search: "))
found=False