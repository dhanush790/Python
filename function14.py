#Write a function to find the LCM of two numbers.
def lcm(num1,num2):
    greater=max(num1,num2)
    while True:
        if greater%num1==0 and greater%num2==0:
            return greater
        greater+=1
num1=int(input("Enter a num1"))
num2=int(input("Enter a num2"))
print(lcm(num1,num2))