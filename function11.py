#Function to Count the Digits in a Number
def count_of_digit(n):
    count=0
    while n>0:
        count=count+1
        n=n//10
    return count
num=int(input("Enter a num"))
print(count_of_digit(num))