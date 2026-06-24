#Reverse a String Using a Loop
text=input("Enter a string")
reverse=""
for i in text:
    reverse=i+reverse
print(reverse)