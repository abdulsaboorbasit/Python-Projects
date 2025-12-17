contacts = {"Name":[], "Phone":[], "Email":[]}

print("<=== Contact Book ===>")
print("1. Add New Contact")
print("2. Search Contact by Name")
print("3. Delete Contact")
print("4. Add Contact to JSON File")
print("5. Load Contacts from JSON File")
print("6. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = int(input("Enter Phone Number: "))
    email = input("Enter Email Id: ")
    contacts["Name"].append(name)
    contacts["Phone"].append(phone)
    contacts["Email"].append(email)
    print("Contact Added Successfully.")

def search_contact():
    name = input("Enter Name to Search: ")
    if name in contacts["Name"]:
        index = contacts["Name"].index(name)
        print(f"Name: {contacts['Name'][index]}\nPhone: {contacts['Phone'][index]}\nEmail: {contacts['Email'][index]}")
    else:
        print("Contact Not Found.")

def delete_contact():
    name = input("Enter Name to Delete: ")
    if name in contacts["Name"]:
        index = contacts["Name"].index(name)
        contacts["Name"].pop(index)
        contacts["Phone"].pop(index)
        contacts["Email"].pop(index)
        print("Contact Deleted Successfully.")
    else:
        print("Contact Not Found.")

def save_to_json():
    import json
    with open("contacts.json", "a") as file:
        json.dump(contacts, file)
    print("Contacts Saved to contacts.json")

def load_from_json():
    import json
    try:
        with open("contacts.json", "r") as file:
            loaded_contacts = json.load(file)
            contacts.update(loaded_contacts)
        for i in range(len(contacts["Name"])):
            print(f"Name: {contacts['Name'][i]}, Phone: {contacts['Phone'][i]}, Email: {contacts['Email'][i]}")
    except FileNotFoundError:
        print("No saved contacts found.")

while True:
    choice = int(input("Enter Your Choice (1-6): "))
    if choice == 1:
        add_contact()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        delete_contact()
    elif choice == 4:
        save_to_json()
    elif choice == 5:
        load_from_json()
    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid Choice. Please Try Again.")