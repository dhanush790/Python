#Write a function to reverse a number.
def reverse(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

n = int(input("Enter a number: "))
print("Reversed Number =", reverse(n))