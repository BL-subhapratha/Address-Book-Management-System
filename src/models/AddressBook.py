from .ContactPerson import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []
    
    #UC2: Add contact to Address Book
    def addNewContact(self):

        #UC5: Add multiple person to address book
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

            newcontact = Contact(newfirstname, newlastname, newcity, newstate, newzip, newphone, newemail)

            #UC7: Check for duplicate contact
            if newcontact in self.contacts:
                print("Contact already exists!")
            else:
                self.contacts.append(newcontact)

        print("----------------------------------------------------------------------------")
        for contact in self.contacts:
            print(contact)

        return self.contacts
    
    #UC3: Edit existing contact
    def editContact(self, contacts):
        editname = input("Enter the name you would like to edit details for: ")
        found = False
        for contact in contacts:
            if contact.fullname == editname:
                found = True
                print("Enter new details of the contact:\n")
                newfirstname = input("First Name: ")
                newlastname = input("Last Name: ")
                newcity = input("City: ")
                newstate = input("State: ")
                newzip = input("Zip: ")
                newphone = input("Phone Number: ")
                newemail = input("Email address: ")

                contact.fullname = newfirstname + " "+ newlastname 
                contact.city = newcity
                contact.state = newstate
                contact.zip = newzip
                contact.phone = newphone
                contact.email = newemail
                break
        if found == False:
            print("Entered name not found in the records!")
        else:
            print("------------------------------------------------------------------------\n")
            print("Records after editing...\n")
            for c in contacts:
                print(c)

    #UC4: Delete person using name
    def deleteContact(self, contacts):
        delName = input("Enter the name you want to delete: ")
        found = False
        for contact in contacts:
            if contact.fullname == delName:
                found = True
                print("Deleting the below details from the record...\n")
                print(contact)
                contacts.remove(contact)
                break
        if found == False:
            print(f"{delName} is not found in the records!")
        else:
            print("----------------------------------------------------------------\n")
            print("Records after deleting...\n")
            for contact in contacts:
                print(contact)