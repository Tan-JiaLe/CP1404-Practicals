PASSWORD_LENGTH = 10

def main():
    """Display * by password length"""
    password = validate_password()
    print(len(password) * "*")

def validate_password():
    """Get validate password"""
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Enter password:")
    return password

main()