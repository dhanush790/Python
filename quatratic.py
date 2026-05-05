import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

D = b**2 - 4*a*c  

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Two Real Roots:", root1, root2)
    
elif D==0:
    root=-b/(2*a)
    print("One real root:",root)

else:
    real = -b / (2*a)
    imaginary = math.sqrt(-D) / (2*a)
    print("Complex Roots:", real, "+", imaginary, "i and", real, "-", imaginary, "i")