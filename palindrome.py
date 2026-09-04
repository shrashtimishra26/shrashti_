text=input("enter your text:")
text=text.lower()
text=text.replace("","")

if text==text[::-1]:
    print("it is a palindrome")
else:
    print("it is not a palindrome ")