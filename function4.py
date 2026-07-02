#Write a function to find the largest of three numbers.
def largest(a,b,c):
    if a>b and a>c:
        return "A is greater"
    elif b>c and b>a:
        return "B is greater"
    else:
        return "C is greater"
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
print(largest(a,b,c))