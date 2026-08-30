import string
password= input("enter your password ")
if len(password)<8:
    print("password must be at least 8 character")
elif not any (c.isupper()for c in password):
    print("password must contain upercase letter ")
elif not any (c.islower()for c in password):
    print("password must contain lowercase letter ")
elif not any (c.isdigit()for c in password):
    print("password must contain a number ")
elif not any (c in string.punctuation for c in password):
    print("password must contain special character")
else:
    print("valid password")


