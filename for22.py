#Least Common Multiple (LCM) of Two Numbers
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
lcm=max(num1,num2)
while True:
    if lcm%num1==0 and lcm%num2==0:
        print(lcm)
        break
    lcm+=1