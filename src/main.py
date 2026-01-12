import json

from src.models.AddressBookMain import createAddressBook, displayAddressBooks
from src.models.AddressBook import AddressBook
from src.models.SearchPerson import SearchPerson
from src.models.ContactPerson import Contact


print("Welcome to Address Book Program!\n")

addressbook = AddressBook()
address_books = {}

while True:
    
    print("\n1. Create Address Book")
    print("2. Display Address Books")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Search Person")
    print("6. Sort Persons")
    print("7. Read/Write to File")
    print("8. Exit")

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
        search_person = SearchPerson(address_books)
        searchchoice = int(input("Enter 1. to search by city or 2. to search by state: "))
        if searchchoice == 1:
            searchcity = input("Enter the city name to search contacts: ")
            search_person.search_person_by_city(searchcity)
        elif searchchoice == 2:
            searchstate = input("Enter the state name to search contacts: ")
            search_person.search_person_by_state(searchstate)
        else:
            print("Invalid choice!")

    elif choice == 6:
        book_name = input("Enter address book name: ")
        if book_name in address_books:
            contacts = address_books[book_name]
            addressbook.sortPerson(contacts)
        else:
            print("Address book not found!\n")

    elif choice == 7:
        whatfile = int(input("Enter 1. for text file 2. for csv file 3. for json file: "))
        if whatfile == 1:
            #UC13: Read or write address book into a file
            filechoice = int(input("Enter 1. to read from file 2. write into file: "))
            if filechoice == 1:
                with open("AddressBook.txt") as rfile:
                    for line in rfile:
                        print(line.strip())
            else:
                with open("AddressBook.txt","a") as wfile:
                    for book_name, contacts in address_books.items():
                        wfile.write(f"\nAddress Book: {book_name}")
                        wfile.write("-" * 40)
                        for c in contacts:
                            wfile.write(f"{c.fullname}, {c.city}, {c.state}, {c.zip}, {c.phone}, {c.email}\n")
        elif whatfile == 2:
            #UC14: Read or write address book to csv file
            filechoice = int(input("Enter 1. to read from file 2. write into file: "))
            if filechoice == 1:
                with open("AddressBook.csv") as rfile:
                    for line in rfile:
                        print(line.strip())
            else:
                with open("AddressBook.csv","a") as wfile:
                    for book_name, contacts in address_books.items():
                        for c in contacts:
                            wfile.write(f"{c.fullname}, {c.city}, {c.state}, {c.zip}, {c.phone}, {c.email}\n")

        else:
            filechoice = int(input("Enter 1. to read from file 2. write into file: "))
            if filechoice == 1:
                with open("AddressBook.json", "r") as rfile:
                    data = json.load(rfile)

                    for book_name, contacts in data.items():
                        print(f"\nAddress Book: {book_name}")
                        print("-" * 40)

                        for c in contacts:
                            print(f"{c['fullname']}, {c['city']}, {c['state']},{c['zip']}, {c['phone']}, {c['email']}")

            else:
                with open("AddressBook.json", "w") as wfile:
                    data = {}

                    for book_name, contacts in address_books.items():
                        data[book_name] = []

                        for c in contacts:
                            data[book_name].append({
                                "fullname": c.fullname,
                                "city": c.city,
                                "state": c.state,
                                "zip": c.zip,
                                "phone": c.phone,
                                "email": c.email
                            })

                    json.dump(data, wfile, indent=4)

    elif choice == 8:
        break

    else:
        print("Invalid choice")