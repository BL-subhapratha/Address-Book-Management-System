from ContactPerson import Contact

class AddressBook:
    def __init__(self):
        self.contact = []
    
    #UC2: Add contact to Address Book
    def addNewContact(self):

        contacts = []
        numContact = int(input("Enter the number of contacts you would like to store: "))
        for i in range(numContact):
            print(f"Enter the below details for contact {i+1}: ")
            newfirstname = input(f"{i+1} First Name: ")
            newlastname = input(f"{i+1} Last Name: ")
            newcity = input(f"{i+1} City: ")
            newstate = input(f"{i+1} State: ")
            newzip = input(f"{i+1} Zip Code: ")
            newphone = input(f"{i+1} Phone Number: ")
            newemail = input(f"{i+1} Email ID: ")

            self.contact = Contact(newfirstname, newlastname, newcity, newstate, newzip, newphone, newemail)
            contacts.append(self.contact)

        print("----------------------------------------------------------------------------")
        for contact in contacts:
            print(contact)

        return contacts
        