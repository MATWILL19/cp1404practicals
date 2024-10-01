MIN_PASSWORD_LENGTH = 1
password = input("Enter a password: ")
password_length = len(password)
if len(password) < MIN_PASSWORD_LENGTH:
    print("Invalid password length")
    password = input("Enter a password: ")
else:
    for i in range(0, password_length):
        print("*", end="")