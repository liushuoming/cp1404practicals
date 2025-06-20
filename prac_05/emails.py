def main():
    """Main program to collect emails and names, then display them."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        extracted_name = get_name_from_email(email)
        confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()

        if confirmation not in ('', 'y'):
            actual_name = input("Name: ").strip()
        else:
            actual_name = extracted_name

        email_to_name[email] = actual_name
        email = input("Email: ").strip()  # ask for the next email

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extract and format a name from an email address."""
    parts = email.split('@')[0]
    name_parts = parts.split('.')
    formatted_name = ' '.join(name_parts).title()
    return formatted_name

if __name__ == "__main__":
    main()