contacts = []


def add_contact():
    """Ask the user for details and append a new contact dictionary to the list."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    print(f"Contact '{name}' added successfully!\n")


def search_contact(name):
    """Search the contacts list by name. Return the matching dictionary, or None."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    """Remove a contact by name, if it exists."""
    contact = search_contact(name)
    if contact is not None:
        contacts.remove(contact)
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print(f"No contact found with the name '{name}'.\n")


def view_all():
    """Display all contacts in a formatted layout."""
    if len(contacts) == 0:
        print("No contacts saved yet.\n")
        return

    print("========= ALL CONTACTS =========")
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("---------------------------------")
    print("=================================\n")

def main():
    while True:
        print("CONTACT BOOK MENU")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_name = input("Enter the name to search for: ")
            result = search_contact(search_name)
            if result is not None:
                print(f"Found: {result['name']}, {result['phone']}, {result['email']}\n")
            else:
                print(f"No contact found with the name '{search_name}'.\n")
        elif choice == "3":
            delete_name = input("Enter the name to delete: ")
            delete_contact(delete_name)
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
