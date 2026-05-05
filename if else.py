#simple calculator
num1=float(input("Enter a num1:"))
num2=float(input("Enter a num2:"))
op=input("Enter operator")
if op =="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
   if(num2!=0):
    print(num1/num2)
else:
    print("Can't divided by zero")

