#UC8: Search person by city or state
class SearchPerson:
    def __init__(self, address_books):
        self.address_books = address_books

    def search_person_by_city(self, city):
        found = False
        print(f"\nPersons found in city: {city}\n")

        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                if contact.city.lower() == city.lower():
                    #UC9: View person by City
                    print(f"Address Book: {book_name}")
                    print(contact)
                    found = True

        if not found:
            print("No persons found in this city.")
        
    def search_person_by_state(self, state):
        found = False
        print(f"\nPersons found in state: {state}\n")

        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                if contact.state.lower() == state.lower():
                    #UC9: View person by State
                    print(f"Address Book: {book_name}")
                    print(contact)
                    found = True

        if not found:
            print("No persons found in this state.")