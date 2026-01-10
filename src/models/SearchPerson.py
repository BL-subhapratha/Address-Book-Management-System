#UC8: Search person by city or state
class SearchPerson:
    def __init__(self, address_books):
        self.address_books = address_books

    def search_person_by_city(self, city):
        countcity = 0
        found = False
        print(f"\nPersons found in city: {city}\n")

        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                if contact.city.lower() == city.lower():
                    #UC9: View person by City
                    print(f"Address Book: {book_name}")
                    print(contact)
                    found = True
                    countcity += 1

        if not found:
            print("No persons found in this city.")
        else:
            #UC10: number of contact persons by city
            print(f"Total number of contacts found in city {city} is",countcity)
        
    def search_person_by_state(self, state):
        countstate = 0
        found = False
        print(f"\nPersons found in state: {state}\n")

        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                if contact.state.lower() == state.lower():
                    #UC9: View person by State
                    print(f"Address Book: {book_name}")
                    print(contact)
                    found = True
                    countstate += 1

        if not found:
            print("No persons found in this state.")
        else:
            #UC10: number of contact persons by state
            print(f"Total number of contacts found in state {state} is",countstate)