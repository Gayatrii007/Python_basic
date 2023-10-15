# Contact Book Application

# Initialize an empty contact list
contacts = []

# Function to add a new contact
def add_contact(name, phone, email, address):
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

# Function to view the contact list
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}")

# Function to search for a contact by name or phone number
def search_contact(query):
    matching_contacts = []
    for contact in contacts:
        if query in contact["Name"] or query in contact["Phone"]:
            matching_contacts.append(contact)
    return matching_contacts

# Function to update a contact
def update_contact(index, name, phone, email, address):
    contact = contacts[index]
    contact["Name"] = name
    contact["Phone"] = phone
    contact["Email"] = email
    contact["Address"] = address
    print(f"Contact updated successfully!")

# Function to delete a contact
def delete_contact(index):
    contact = contacts.pop(index)
    print(f"Contact {contact['Name']} deleted!")

# Main application loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        add_contact(name, phone, email, address)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        query = input("Search by Name or Phone: ")
        matching_contacts = search_contact(query)
        if matching_contacts:
            print("Matching Contacts:")
            for idx, contact in enumerate(matching_contacts, start=1):
                print(f"{idx}. Name: {contact['Name']}, Phone: {contact['Phone']}")
        else:
            print("No matching contacts found.")

    elif choice == "4":
        index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            name = input("Enter New Name: ")
            phone = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            address = input("Enter New Address: ")
            update_contact(index, name, phone, email, address)
        else:
            print("Invalid index. Please enter a valid index.")

    elif choice == "5":
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            delete_contact(index)
        else:
            print("Invalid index. Please enter a valid index.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
