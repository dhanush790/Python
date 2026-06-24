#Print a right-angled star pattern.
rows=int(input("Enter a rows"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()