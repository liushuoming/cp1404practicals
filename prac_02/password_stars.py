"""
min password length = 8
get password
while len(password) < min password length
print "make sure your password length > min password length"
get password
print" '*' * len(password)"
"""
min_password_length = 8
password = input("enter your password")
while len(password) < min_password_length:
    print("make sure your password length > min password length")
    password = input("enter your password")
    print("*" * len(password))