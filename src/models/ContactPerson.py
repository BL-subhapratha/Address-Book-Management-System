#UC1: Create contact class
class Contact:
    def __init__(self, first_name, last_name, city, state, zip, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.fullname = first_name + " " + last_name
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Full Name: {self.fullname}\nAddress: {self.city}, {self.state}, {self.zip}\nPhone Number: {self.phone}\nEmail: {self.email}\n"