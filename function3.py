#Write a function to check whether a number is even or odd.
def evenodd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    return n
num=int(input("Enter a num"))
print(evenodd(num))


    