from src.models.AddressBookMain import createAddressBook, displayAddressBooks
from src.models.AddressBook import AddressBook
#from models.ContactPerson import Contact


print("Welcome to Address Book Program!\n")

addressbook = AddressBook()
address_books = {}

while True:
    
    print("\n1. Create Address Book")
    print("2. Display Address Books")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        address_books = createAddressBook()

    elif choice == 2:
        displayAddressBooks()

    elif choice == 3:
        bookname = input("Enter address book name: ")
        if bookname in address_books:
            contacts = address_books[bookname]
            addressbook.editContact(contacts)
        else:
            print("Address book not found!\n")

    elif choice == 4:
        book_name = input("Enter address book name: ")
        if book_name in address_books:
            contacts = address_books[book_name]
            addressbook.deleteContact(contacts)
        else:
            print("Address book not found!\n")

    elif choice == 5:
        break

    else:
        print("Invalid choice")