"""
Word Occurrences
Estimate: 40 minutes
Actual:   45 minutes
"""

def main():
    """Get and print names from users inputted emails"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_suggestion = input(f"Is your name {name}? (Y/n) ").upper()
        if name_suggestion.upper() != "Y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Get name from email"""
    email_first_parts = email.split('@')[0]
    email_second_parts = email_first_parts.split('.')
    name = " ".join(email_second_parts).title()
    return name

main()