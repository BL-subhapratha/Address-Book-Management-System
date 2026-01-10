from .AddressBook import AddressBook

#UC6: Add multiple address book
address_books = {}
addressbook = AddressBook()

def createAddressBook():
    book_name = input("\nEnter Address Book name: ")

    contacts = addressbook.addNewContact()

    address_books[book_name] = contacts
    return address_books


def displayAddressBooks():
    for book_name, contacts in address_books.items():
        print(f"\nAddress Book: {book_name}")
        print("-" * 40)

        for contact in contacts:
            print(contact)