""""""
def main():
    """Get names from emails and store them in dictionary"""
    email_to_name = {}
    email = input("Email: ")
    try:
        name = get_name_from_email(email)
        name_suggestion = input(f"Is your name {name}? (Y/n")


def get_name_from_email():
    """Get names from inputted email"""
