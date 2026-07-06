#Function to Reverse a String
def reverse_string(text):
    reverse=""
    for i in text:
        reverse=i+reverse
    return reverse
text=input("Enter text:")
print(reverse_string(text))