rows = int(input("Enter rows"))
cols = int(input("Enter cols"))

A = []
B = []
C = []

print("Enter Matrix A:")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

print("Enter Matrix B:")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        sum = 0
        for k in range(cols):
            sum += A[i][k] * B[k][j]
        row.append(sum)
    C.append(row)

print("Result:")

for i in range(rows):
    for j in range(cols):
        print(C[i][j], end=" ")
    print()