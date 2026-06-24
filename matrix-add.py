rows=int(input("Enter a row"))
cols=int(input("Enter a col"))
A=[]
B=[]
C=[]

print("Enter elements of Matrix A:")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    B.append(row)

for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(A[i][j]+B[i][j])
    C.append(row)
print("Result Matrix:")

for i in range(rows):
    for j in range(cols):
        print(C[i][j],end=" ")
    print()