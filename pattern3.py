#Print a square star pattern.
rows=int(input("Enter a row"))
for i in range(rows):
    for j in range(rows):
        print("*",end=" ")
    print()