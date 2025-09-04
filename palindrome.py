text = input("Enter a string or number: ")

if text == text[::-1]:
    print(text, "is a Palindrome")
else:
    print(text, "is Not a Palindrome")
