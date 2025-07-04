#  Contact Book  
# Contact Information: Store name, phone number, email, and address for each contact.
#  Add Contact: Allow users to add new contacts with their details.
#  View Contact List: Display a list of all saved contacts with names and phone numbers.
#  Search Contact: Implement a search function to find contacts by name or phone number.
#  Update Contact: Enable users to update contact details.
#  Delete Contact: Provide an option to delete a contact.
#  User Interface: Design a user-friendly interface for easy interaction.


import json
import os

# File to store contacts
CONTACT_FILE = "my_contacts.cbook"

# Load existing contacts from file
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        try:
            with open(CONTACT_FILE, 'r') as file:
                return json.load(file)
        except:
            print("Error: Contact file corrupted. Starting with empty contact list.")
            return []
    else:
        return []

# Save contacts to file
def save_contacts(contacts):
    try:
        with open(CONTACT_FILE, 'w') as file:
            json.dump(contacts, file, indent=4)
    except:
        print("Error: Could not save contacts.")

# Show contact details nicely
def show_contact(contact):
    print("\n--- Contact Details ---")
    print(f"Name    : {contact['name']}")
    print(f"Phone   : {contact['phone']}")
    print(f"Email   : {contact.get('email', 'Not provided')}")
    print(f"Address : {contact.get('address', 'Not provided')}")
    print(f"Company : {contact.get('company', 'Not provided')}")

# Add a new contact
def add_contact(contacts):
    print("\nAdd New Contact")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()
    address = input("Address (optional): ").strip()
    company = input("Company (optional): ").strip()

    contact = {
        'name': name,
        'phone': phone,
        'email': email if email else None,
        'address': address if address else None,
        'company': company if company else None
    }

    contacts.append(contact)
    save_contacts(contacts)
    print(f"\nContact {name} added successfully!")

# Search for contacts
def search_contacts(contacts):
    print("\nSearch Contact")
    search_term = input("Enter name or phone: ").lower()

    found = []
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            found.append(contact)

    if not found:
        print("No contact found.")
        return []

    for idx, contact in enumerate(found, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    
    return found

# View all contacts
def view_contacts(contacts):
    print("\nAll Contacts")
    if not contacts:
        print("Contact book is empty.")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']:20} {contact['phone']:15}")
    
    choice = input("\nEnter contact number to view details (or press Enter to skip): ")
    if choice.isdigit():
        number = int(choice)
        if 1 <= number <= len(contacts):
            show_contact(contacts[number - 1])
        else:
            print("Invalid contact number.")

# Update contact
def update_contact(contacts):
    found = search_contacts(contacts)
    if not found:
        return

    try:
        choice = int(input("\nEnter contact number to update: "))
        if 1 <= choice <= len(found):
            contact_to_update = found[choice - 1]

            print("\nLeave blank to keep existing information.")
            new_name = input(f"Name ({contact_to_update['name']}): ").strip()
            new_phone = input(f"Phone ({contact_to_update['phone']}): ").strip()
            new_email = input(f"Email ({contact_to_update.get('email', 'Not provided')}): ").strip()
            new_address = input(f"Address ({contact_to_update.get('address', 'Not provided')}): ").strip()
            new_company = input(f"Company ({contact_to_update.get('company', 'Not provided')}): ").strip()

            if new_name:
                contact_to_update['name'] = new_name
            if new_phone:
                contact_to_update['phone'] = new_phone
            if new_email:
                contact_to_update['email'] = new_email
            if new_address:
                contact_to_update['address'] = new_address
            if new_company:
                contact_to_update['company'] = new_company

            save_contacts(contacts)
            print("\nContact updated successfully!")
        else:
            print("Invalid number selected.")
    except:
        print("Invalid input.")

# Delete contact
def delete_contact(contacts):
    found = search_contacts(contacts)
    if not found:
        return

    try:
        choice = int(input("\nEnter contact number to delete: "))
        if 1 <= choice <= len(found):
            contact_to_delete = found[choice - 1]
            confirm = input(f"Are you sure you want to delete {contact_to_delete['name']}? (y/n): ").lower()

            if confirm == 'y':
                contacts.remove(contact_to_delete)
                save_contacts(contacts)
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid number selected.")
    except:
        print("Invalid input.")

def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. View All Contacts")
    print("2. Add New Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def run_contact_book():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nThank you for using Contact Book. Goodbye!")
            break
        else:
            print("Please choose a valid option (1-6).")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    run_contact_book()


