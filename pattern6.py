#Print an inverted pyramid pattern.
rows=int(input("Enter a row:"))
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()