MIN_PASSWORD_LENGTH = 1

def main():
    password = get_password()
    print_password(password)

def get_password():
    password = input("Enter a password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print("Invalid password length")
        get_password()
    return password

def print_password(password):
    for i in range(0, len(password)):
        print("*", end="")

main()